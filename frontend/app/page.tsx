import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-6xl font-bold text-white mb-6 drop-shadow-lg">
          🦸 Superhero Photo Booth
        </h1>
        <p className="text-xl text-gray-300 mb-12 max-w-2xl mx-auto">
          Transform yourself into your favorite movie character! 
          Upload or capture your photo and watch the magic happen.
        </p>
        <Link 
          href="/booth"
          className="inline-block bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold py-4 px-8 rounded-full text-lg hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 shadow-xl"
        >
          Start Photo Booth →
        </Link>
      </div>
    </div>
  )
}
