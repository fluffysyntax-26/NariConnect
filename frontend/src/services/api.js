const API_URL = import.meta.env.VITE_API_URL;

export const chatWithAI = async (message, token, chatHistory = [], userProfile = {}) => {
  if (!token) {
    throw new Error('User not authenticated');
  }

  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ 
        message,
        chat_history: chatHistory,
        user_profile: userProfile
      })
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Chat API Error:', error);
    throw error;
  }
};

export const fetchSchemes = async (token, page = 1, filters = {}) => {
  if (!token) {
    throw new Error('User not authenticated');
  }

  const queryParams = new URLSearchParams({
    page: page.toString(),
    limit: '10',
    ...filters
  });

  try {
    const response = await fetch(`${API_URL}/schemes?${queryParams.toString()}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Fetch Schemes Error:', error);
    throw error;
  }
};

export const fetchSchemeDetails = async (token, slug) => {
  if (!token) {
    throw new Error('User not authenticated');
  }

  try {
    const response = await fetch(`${API_URL}/schemes/${slug}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Fetch Scheme Details Error:', error);
    throw error;
  }
};
