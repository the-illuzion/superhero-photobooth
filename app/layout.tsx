import './globals.css'

export const metadata = {
  title: 'Superhero Photobooth',
  description: 'A photobooth app for superheroes',
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
