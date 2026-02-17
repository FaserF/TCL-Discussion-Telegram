/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        tcl: {
          dark: '#050507',
          card: '#1a1a1c',
          red: '#e00109',
          accent: '#ff4d4d',
        }
      },
    },
  },
  plugins: [],
}
