if [ -n "$APPVEYOR_REPO_TAG_NAME" ]; then
    export PKG_VER="${APPVEYOR_REPO_TAG_NAME#v}" # Remove the 'v' prefix
    export BUILD_VER="$PKG_VER"
else
    # Get the latest Git tag and handle missing tags gracefully
    cv=$(git describe --abbrev=0 2>/dev/null || echo "v0.0.0") # Default to v1.0.0 if no tag
    cv=${cv#v} # Remove the 'v' prefix if present
    major=$(echo "$cv" | cut -d. -f1)
    minor=$(echo "$cv" | cut -d. -f2)
    minor=$((minor + 1))
    export PKG_VER="${major}.${minor}.0"
    export BUILD_VER="${PKG_VER}+${APPVEYOR_BUILD_NUMBER}"
fi
export PYPI_VER="${BUILD_VER/+/.dev}"
appveyor UpdateBuild -Version $BUILD_VER