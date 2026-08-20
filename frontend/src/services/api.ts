import axios from 'axios'
import { engagementData, modelData, posts, stats, topics, trendData } from '../data/mockData'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 8000,
})

export const analyzeTopic = async (topic: string) => {
  try {
    const response = await api.post('/analyze', { topic })
    return response.data
  } catch {
    return { topic, posts: 12480, status: 'demo' }
  }
}

export const getDashboard = async () => ({ stats, trendData, topics, posts })
export const getAnalytics = async () => ({ trendData, topics, modelData, engagementData })
export const getPosts = async () => posts
export const getHistory = async () => [
  { topic: 'Tesla', analyzed: '2,450 posts', sentiment: 'Positive', date: 'Today' },
  { topic: 'OpenAI', analyzed: '1,820 posts', sentiment: 'Positive', date: 'Yesterday' },
  { topic: 'Bitcoin', analyzed: '3,100 posts', sentiment: 'Neutral', date: 'Aug 16, 2025' },
]
export const getHealthStatus = async () => ({ connected: false, label: 'Demo Data' })

export default api
