import type { NextApiRequest, NextApiResponse } from 'next';
import axios from 'axios';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    // Make the API request to the backend server
    const response = await axios.get('http://localhost:8000/points', {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Return the data from the backend to the frontend
    res.status(200).json(response.data);
  } catch (error) {
    console.error('Error fetching points:', error);
    res.status(500).json({ error: 'Error fetching points from the server' });
  }
}
