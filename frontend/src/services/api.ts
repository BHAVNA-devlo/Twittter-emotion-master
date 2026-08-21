import axios from 'axios'

export type AnalysisPost = {
  id: string
  text: string
  created_at: string
  sentiment: 'Positive' | 'Neutral' | 'Negative'
  emotion: string
  polarity: number
  subjectivity: number
  confidence: number
  author?: string | null
}

export type AnalysisResponse = {
  query: string
  total_posts: number
  demo_mode: boolean
  sentiment: { positive: number; negative: number; neutral: number }
  emotions: Record<string, number>
  average_polarity: number
  average_subjectivity: number
  posts: AnalysisPost[]
}

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 8000,
})

export const analyzeTopic = async (topic: string) => {
  const response = await api.get<AnalysisResponse>('/api/analyze', { params: { query: topic } })
  return response.data
}

export const getHealthStatus = async () => {
  const response = await api.get('/api/health')
  return response.data
}

export default api
