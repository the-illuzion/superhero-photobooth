import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Superhero Photo Booth',
  description: 'Transform yourself into your favorite superhero',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
