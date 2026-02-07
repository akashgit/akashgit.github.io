#!/bin/bash
# install.sh - Setup development environment for akashgit.github.io

set -e

echo "🚀 Setting up akashgit.github.io development environment..."
echo ""

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed"
    echo "   Please install Node.js 20+ from https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "⚠️  Node.js version is too old (requires 18+)"
    echo "   Current version: $(node -v)"
    exit 1
fi
echo "✅ Node.js $(node -v)"

# Check for Ruby
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby is not installed"
    echo "   Please install Ruby 3.0+ from https://www.ruby-lang.org/"
    echo "   Or use rbenv: brew install rbenv && rbenv install 3.2.0"
    exit 1
fi

RUBY_VERSION=$(ruby -v | cut -d' ' -f2)
RUBY_MAJOR=$(echo $RUBY_VERSION | cut -d'.' -f1)
RUBY_MINOR=$(echo $RUBY_VERSION | cut -d'.' -f2)

if [ "$RUBY_MAJOR" -lt 3 ]; then
    echo "❌ Ruby version is too old (requires 3.0+)"
    echo "   Current version: $RUBY_VERSION"
    echo ""
    echo "   To install a newer Ruby version:"
    echo "   1. Install rbenv: brew install rbenv ruby-build"
    echo "   2. Install Ruby 3.2: rbenv install 3.2.0"
    echo "   3. Set as default: rbenv global 3.2.0"
    echo "   4. Restart your terminal and run this script again"
    exit 1
fi
echo "✅ Ruby $RUBY_VERSION"

# Check for Bundler
if ! command -v bundle &> /dev/null; then
    echo "📦 Installing Bundler..."
    gem install bundler
fi
echo "✅ Bundler $(bundle -v | cut -d' ' -f3)"

# Install Node dependencies
echo ""
echo "📦 Installing Node dependencies..."
npm install

# Install Ruby dependencies (locally isolated)
echo ""
echo "📦 Installing Ruby dependencies to local vendor/bundle..."
echo "   (This keeps gems isolated from your system Ruby)"
bundle config set --local path 'vendor/bundle'
bundle install

# Build Tailwind CSS
echo ""
echo "🎨 Building Tailwind CSS..."
npm run build:css

echo ""
echo "✅ Installation complete!"
echo ""
echo "To start the development server, run:"
echo "   npm run serve"
echo ""
echo "The site will be available at http://localhost:4000"
