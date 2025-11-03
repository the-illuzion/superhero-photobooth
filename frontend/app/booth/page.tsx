'use client'

import { useState, useRef, useCallback } from 'react'
import Webcam from 'react-webcam'

const CHARACTERS = [
  { id: 'ironman', name: 'Iron Man', image: '/characters/ironman.jpg' },
  { id: 'spiderman', name: 'Spider-Man', image: '/characters/spiderman.jpg' },
  { id: 'batman', name: 'Batman', image: '/characters/batman.jpg' },
  { id: 'wonderwoman', name: 'Wonder Woman', image: '/characters/wonderwoman.jpg' },
]

export default function BoothPage() {
  const [captureMode, setCaptureMode] = useState<'webcam' | 'upload' | null>(null)
  const [userImage, setUserImage] = useState<string | null>(null)
  const [selectedCharacter, setSelectedCharacter] = useState<string>('')
  const [isProcessing, setIsProcessing] = useState(false)
  const [resultImage, setResultImage] = useState<string | null>(null)
  const webcamRef = useRef<Webcam>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const capturePhoto = useCallback(() => {
    const imageSrc = webcamRef.current?.getScreenshot()
    if (imageSrc) {
      setUserImage(imageSrc)
      setCaptureMode(null)
    }
  }, [webcamRef])

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onloadend = () => {
        setUserImage(reader.result as string)
        setCaptureMode(null)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleSubmit = async () => {
    if (!userImage || !selectedCharacter) {
      alert('Please capture/upload an image and select a character!')
      return
    }

    setIsProcessing(true)
    
    try {
      // Convert base64 to blob
      const response = await fetch(userImage)
      const blob = await response.blob()
      
      const formData = new FormData()
      formData.append('user_image', blob, 'user.jpg')
      formData.append('character', selectedCharacter)

      const apiResponse = await fetch('http://localhost:8000/api/morph', {
        method: 'POST',
        body: formData,
      })

      if (!apiResponse.ok) {
        throw new Error('Failed to process image')
      }

      const data = await apiResponse.json()
      setResultImage(data.result_image)
    } catch (error) {
      console.error('Error:', error)
      alert('Failed to process image. Make sure the backend server is running.')
    } finally {
      setIsProcessing(false)
    }
  }

  const resetAll = () => {
    setUserImage(null)
    setSelectedCharacter('')
    setResultImage(null)
    setCaptureMode(null)
  }

  const retakePhoto = () => {
    setUserImage(null)
    setResultImage(null)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-5xl font-bold text-white text-center mb-8">
          🦸 Superhero Photo Booth
        </h1>

        {!resultImage ? (
          <div className="grid md:grid-cols-2 gap-8">
            {/* Left Panel - Image Capture */}
            <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 border border-white/20">
              <h2 className="text-2xl font-semibold text-white mb-4">Step 1: Your Photo</h2>
              
              {!userImage && !captureMode && (
                <div className="space-y-4">
                  <button
                    onClick={() => setCaptureMode('webcam')}
                    className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-4 px-6 rounded-lg transition-all"
                  >
                    📷 Use Webcam
                  </button>
                  <button
                    onClick={() => fileInputRef.current?.click()}
                    className="w-full bg-purple-500 hover:bg-purple-600 text-white font-bold py-4 px-6 rounded-lg transition-all"
                  >
                    📁 Upload Photo
                  </button>
                  <input
                    ref={fileInputRef}
                    type="file"
                    accept="image/*"
                    onChange={handleFileUpload}
                    className="hidden"
                  />
                </div>
              )}

              {captureMode === 'webcam' && (
                <div className="space-y-4">
                  <Webcam
                    ref={webcamRef}
                    screenshotFormat="image/jpeg"
                    className="w-full rounded-lg"
                    videoConstraints={{ facingMode: 'user' }}
                  />
                  <div className="flex gap-2">
                    <button
                      onClick={capturePhoto}
                      className="flex-1 bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-lg"
                    >
                      Capture
                    </button>
                    <button
                      onClick={() => setCaptureMode(null)}
                      className="flex-1 bg-gray-500 hover:bg-gray-600 text-white font-bold py-3 px-6 rounded-lg"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              )}

              {userImage && (
                <div className="space-y-4">
                  <img src={userImage} alt="Your photo" className="w-full rounded-lg" />
                  <button
                    onClick={retakePhoto}
                    className="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 px-6 rounded-lg"
                  >
                    Retake Photo
                  </button>
                </div>
              )}
            </div>

            {/* Right Panel - Character Selection */}
            <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 border border-white/20">
              <h2 className="text-2xl font-semibold text-white mb-4">Step 2: Choose Character</h2>
              
              <div className="grid grid-cols-2 gap-4">
                {CHARACTERS.map((char) => (
                  <button
                    key={char.id}
                    onClick={() => setSelectedCharacter(char.id)}
                    className={`p-4 rounded-lg border-2 transition-all ${
                      selectedCharacter === char.id
                        ? 'border-yellow-400 bg-yellow-400/20'
                        : 'border-white/30 hover:border-white/50'
                    }`}
                  >
                    <div className="aspect-square bg-gray-700 rounded-lg mb-2 flex items-center justify-center text-4xl">
                      {char.name[0]}
                    </div>
                    <p className="text-white font-semibold text-center">{char.name}</p>
                  </button>
                ))}
              </div>

              <button
                onClick={handleSubmit}
                disabled={!userImage || !selectedCharacter || isProcessing}
                className="w-full mt-6 bg-gradient-to-r from-green-500 to-blue-500 hover:from-green-600 hover:to-blue-600 disabled:from-gray-500 disabled:to-gray-600 text-white font-bold py-4 px-6 rounded-lg transition-all disabled:cursor-not-allowed"
              >
                {isProcessing ? '⚡ Processing Magic...' : '✨ Transform Me!'}
              </button>
            </div>
          </div>
        ) : (
          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 border border-white/20">
            <h2 className="text-3xl font-semibold text-white mb-6 text-center">
              🎉 Your Superhero Transformation!
            </h2>
            
            <div className="max-w-2xl mx-auto">
              <img src={resultImage} alt="Result" className="w-full rounded-lg shadow-2xl mb-6" />
              
              <div className="flex gap-4">
                <button
                  onClick={() => {
                    const link = document.createElement('a')
                    link.href = resultImage
                    link.download = 'superhero-transformation.jpg'
                    link.click()
                  }}
                  className="flex-1 bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-lg"
                >
                  💾 Download Image
                </button>
                <button
                  onClick={retakePhoto}
                  className="flex-1 bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 px-6 rounded-lg"
                >
                  📸 Try Another Character
                </button>
                <button
                  onClick={resetAll}
                  className="flex-1 bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-lg"
                >
                  🔄 Start Over
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
