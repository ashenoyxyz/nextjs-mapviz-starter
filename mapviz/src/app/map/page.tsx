"use client";

import 'leaflet/dist/leaflet.css';
import React, { useState, useEffect } from "react";
import dynamic from "next/dynamic";
import axios from "axios"; // Import axios
import { useRouter } from "next/navigation";
import L from "leaflet";

// Dynamically import MapContainer and other components to prevent SSR issues
const MapContainer = dynamic(() => import("react-leaflet").then(mod => mod.MapContainer), { ssr: false });
const TileLayer = dynamic(() => import("react-leaflet").then(mod => mod.TileLayer), { ssr: false });
const Marker = dynamic(() => import("react-leaflet").then(mod => mod.Marker), { ssr: false });
const Popup = dynamic(() => import("react-leaflet").then(mod => mod.Popup), { ssr: false });

// Custom red dot marker icon
const redDotIcon = new L.Icon({
  iconUrl: "/images/red-circle.svg", // Red dot image stored in your public folder
  iconSize: [12, 12], // Size of the red dot
  iconAnchor: [6, 6], // Center the dot (half the size)
  popupAnchor: [0, -6], // Adjust where the popup appears
});

const Map: React.FC = () => {
  const router = useRouter(); // Initialize the router if you need to use it for navigation

  const [points, setPoints] = useState<
    { description: string; lat: number; lng: number }[]
  >([]);
  const [loading, setLoading] = useState(true); // Track loading state
  const [error, setError] = useState<string | null>(null); // Track error state

  // Fetch points from the backend API on component mount using axios
  useEffect(() => {
    const fetchPoints = async () => {
      try {
        // Make a request to the Next.js API that proxies your backend
        const response = await axios.get("/api/points");
        setPoints(response.data); // Update points state with fetched data
        setLoading(false); // Set loading state to false after successful fetch
      } catch (error: any) {
        console.error("Error fetching points:", error.response ? error.response.data : error.message);
        setError(error.response ? error.response.data.error : error.message); // Handle error
        setLoading(false); // Set loading state to false even if there's an error
      }
    };

    fetchPoints(); // Fetch points when the component mounts
  }, []); // Empty dependency array ensures this runs only once

  if (loading) {
    return <div>Loading...</div>; // Display loading state
  }

  if (error) {
    return <div>Error: {error}</div>; // Display error if it occurs
  }

  return (
    <div className="min-h-screen flex">
      {/* Left Pane: Map */}
      <div className="w-1/2 h-screen">
        <MapContainer
          center={[37.0902, -95.7129]} // Default center (USA)
          zoom={4}
          className="h-full w-full"
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          {points.map((point, index) => (
            <Marker
              key={index} // Unique key for each marker
              position={[point.lat, point.lng]} // Set the position using lat/lng from the points array
              icon={redDotIcon} // Use the custom red dot icon
            >
              <Popup>{point.description}</Popup> {/* Show description on marker click */}
            </Marker>
          ))}
        </MapContainer>
      </div>

      {/* Right Pane: List of Points */}
      <div className="w-1/2 h-screen p-4 overflow-auto bg-gray-100 text-black">
        <h1 className="text-2xl font-bold mb-4">Points</h1>
        <ul>
          {points.map((point, index) => (
            <li key={index}>
              <h3 className="text-xl font-bold text-blue-600">
                {point.description}
              </h3>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Map;

