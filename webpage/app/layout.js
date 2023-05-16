import NavBar from '@components/NavBar'
import './globals.css' // import global styles


export const metadata = {
  title: 'SEC BOOKING',
  description: 'Used to book classes, exams and view answer sheets for SEC students',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <NavBar />
        {children} {/* page */}
      </body>
    </html>
  )
}
