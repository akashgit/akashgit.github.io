#!/bin/bash
# test-local.sh - Test local installation

set -e

echo "🧪 Testing local installation..."
echo ""

# Check dependencies
echo "Checking dependencies..."
command -v node >/dev/null 2>&1 || { echo "❌ Node.js not found"; exit 1; }
command -v ruby >/dev/null 2>&1 || { echo "❌ Ruby not found"; exit 1; }
command -v bundle >/dev/null 2>&1 || { echo "❌ Bundler not found"; exit 1; }
echo "✅ All dependencies found"
echo "   Node.js: $(node -v)"
echo "   Ruby: $(ruby -v | cut -d' ' -f1-2)"
echo "   Bundler: $(bundle -v)"

# Check node_modules
echo ""
echo "Checking installations..."
if [ ! -d "node_modules" ]; then
    echo "❌ node_modules not found. Run ./install.sh first"
    exit 1
fi
echo "✅ Node modules installed"

# Check vendor/bundle or .bundle
if [ ! -d "vendor/bundle" ] && [ ! -d ".bundle" ]; then
    echo "⚠️  Ruby gems may not be installed. Checking with bundle..."
    bundle check || {
        echo "❌ Ruby gems not installed. Run ./install.sh first"
        exit 1
    }
fi
echo "✅ Ruby gems installed"

# Check CSS input file exists
if [ ! -f "css/input.css" ]; then
    echo "⚠️  css/input.css not found (will be created in Issue #3)"
    echo "   Skipping CSS compilation test"
else
    # Check CSS was built
    if [ ! -f "css/main.css" ]; then
        echo "❌ css/main.css not found. Run npm run build:css"
        exit 1
    fi
    echo "✅ Tailwind CSS compiled"
fi

# Test Jekyll build
echo ""
echo "Testing Jekyll build..."
if bundle exec jekyll build --quiet 2>&1 | grep -q "Error\|ERROR"; then
    echo "❌ Jekyll build failed"
    bundle exec jekyll build
    exit 1
fi
echo "✅ Jekyll build successful"

# Check _site was created
if [ ! -d "_site" ]; then
    echo "❌ _site directory not created"
    exit 1
fi
echo "✅ Site built to _site/"

echo ""
echo "✅ All tests passed!"
echo ""
echo "To start the development server:"
echo "   npm run serve"
echo ""
echo "Or just Jekyll without CSS watching:"
echo "   bundle exec jekyll serve"
