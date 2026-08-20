export type Sentiment = 'Positive' | 'Neutral' | 'Negative'

export type SocialPost = {
  id: number
  username: string
  handle: string
  time: string
  text: string
  sentiment: Sentiment
  confidence: number
  likes: string
  reposts: number
  replies: number
}

export const trendData = [
  { time: '00:00', positive: 48, neutral: 29, negative: 23 },
  { time: '04:00', positive: 52, neutral: 25, negative: 23 },
  { time: '08:00', positive: 55, neutral: 24, negative: 21 },
  { time: '12:00', positive: 58, neutral: 23, negative: 19 },
  { time: '16:00', positive: 62, neutral: 22, negative: 16 },
  { time: '20:00', positive: 64, neutral: 23, negative: 13 },
]

export const topics = [
  { name: 'Technology', mentions: '4,280', score: 88, sentiment: 'Positive' as Sentiment },
  { name: 'Product', mentions: '3,140', score: 72, sentiment: 'Positive' as Sentiment },
  { name: 'Pricing', mentions: '1,920', score: 54, sentiment: 'Neutral' as Sentiment },
  { name: 'Performance', mentions: '1,340', score: 43, sentiment: 'Positive' as Sentiment },
  { name: 'Support', mentions: '860', score: 31, sentiment: 'Negative' as Sentiment },
]

export const posts: SocialPost[] = [
  { id: 1, username: 'Maya Chen', handle: '@mayacreates', time: '8 min ago', text: 'The latest launch is genuinely impressive. Everything feels faster, clearer, and more thoughtful.', sentiment: 'Positive', confidence: 94, likes: '1.2K', reposts: 248, replies: 93 },
  { id: 2, username: 'Jordan Lee', handle: '@jordanbuilds', time: '22 min ago', text: 'Trying to understand the new pricing tiers. The value is there, but the jump is hard to explain to my team.', sentiment: 'Neutral', confidence: 87, likes: '842', reposts: 96, replies: 41 },
  { id: 3, username: 'Sofia Patel', handle: '@sofiap', time: '41 min ago', text: 'Support got back to me in under ten minutes. That is how you turn a frustrating moment around.', sentiment: 'Positive', confidence: 91, likes: '623', reposts: 72, replies: 18 },
  { id: 4, username: 'Noah Williams', handle: '@nwilliams', time: '1 hr ago', text: 'The dashboard keeps timing out when I try to export. Has anyone else run into this today?', sentiment: 'Negative', confidence: 89, likes: '418', reposts: 54, replies: 36 },
]

export const modelData = [
  { name: 'TextBlob', accuracy: 78, precision: 74, recall: 71, f1: 72 },
  { name: 'VADER', accuracy: 84, precision: 82, recall: 80, f1: 81 },
  { name: 'Advanced NLP', accuracy: 92, precision: 90, recall: 89, f1: 89 },
]

export const engagementData = [
  { engagement: 180, sentiment: 82, topic: 'Product' },
  { engagement: 310, sentiment: 68, topic: 'Technology' },
  { engagement: 420, sentiment: 44, topic: 'Pricing' },
  { engagement: 540, sentiment: 76, topic: 'Performance' },
  { engagement: 690, sentiment: 31, topic: 'Support' },
  { engagement: 820, sentiment: 88, topic: 'Product' },
]

export const stats = [
  { label: 'Total posts', value: '12,480', change: '+18.4%', direction: 'up' },
  { label: 'Positive sentiment', value: '64.2%', change: '+6.8%', direction: 'up' },
  { label: 'Neutral sentiment', value: '22.7%', change: '-2.1%', direction: 'down' },
  { label: 'Negative sentiment', value: '13.1%', change: '-4.7%', direction: 'down' },
]
