/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './_layouts/**/*.html',
    './_includes/**/*.html',
    './_posts/**/*.md',
    './*.md',
    './*.html',
    './blog/**/*.{html,md}',
    './research/**/*.{html,md}',
    './media/**/*.{html,md}',
    './projects/**/*.{html,md}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
          950: '#172554',
        },
        neutral: {
          50: '#fafafa',
          100: '#f5f5f5',
          200: '#e5e5e5',
          300: '#d4d4d4',
          400: '#a3a3a3',
          500: '#737373',
          600: '#525252',
          700: '#404040',
          800: '#262626',
          900: '#171717',
          950: '#0a0a0a',
        },
      },
      fontFamily: {
        sans: [
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          'sans-serif',
        ],
        serif: [
          'Georgia',
          'Cambria',
          '"Times New Roman"',
          'Times',
          'serif',
        ],
        mono: [
          'ui-monospace',
          'SFMono-Regular',
          '"SF Mono"',
          'Menlo',
          'Consolas',
          '"Liberation Mono"',
          'monospace',
        ],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '75ch',
            color: '#404040',
            fontSize: '18px',
            lineHeight: '1.7',
            p: {
              marginBottom: '1.25em',
            },
            a: {
              color: '#1e40af',
              textDecoration: 'none',
              fontWeight: '500',
              '&:hover': {
                color: '#1d4ed8',
                textDecoration: 'underline',
              },
            },
            'h1, h2, h3, h4, h5, h6': {
              fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
              fontWeight: '600',
              color: '#171717',
            },
            h2: {
              fontSize: '1.875rem',
              marginTop: '2em',
              marginBottom: '1em',
            },
            h3: {
              fontSize: '1.5rem',
              marginTop: '1.75em',
              marginBottom: '0.75em',
            },
            code: {
              color: '#404040',
              backgroundColor: '#f5f5f5',
              padding: '0.25em 0.375em',
              borderRadius: '0.25rem',
              fontWeight: '400',
            },
            'code::before': {
              content: '""',
            },
            'code::after': {
              content: '""',
            },
            blockquote: {
              fontStyle: 'italic',
              borderLeftColor: '#2563eb',
              borderLeftWidth: '4px',
              paddingLeft: '1.5rem',
              color: '#525252',
            },
            strong: {
              color: '#171717',
              fontWeight: '600',
            },
            ul: {
              listStyleType: 'disc',
            },
            'ul > li::marker': {
              color: '#2563eb',
            },
          },
        },
        lg: {
          css: {
            fontSize: '1.125rem',
            lineHeight: '1.7',
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
