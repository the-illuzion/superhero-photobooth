/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: (() => {
    const path = process.env.NEXT_PUBLIC_BASE_PATH || '';
    // Ensure basePath is safe: must start with / and contain only valid URL path characters
    if (path && (!path.startsWith('/') || !/^\/[\w-]+$/.test(path))) {
      console.warn(`Invalid basePath "${path}", using empty string`);
      return '';
    }
    return path;
  })(),
  trailingSlash: true,
}

module.exports = nextConfig
