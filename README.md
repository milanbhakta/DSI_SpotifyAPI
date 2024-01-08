# Spotify Data Analysis Package

This Python package facilitates the retrieval of data from the Spotify API and provides tools for analysis.

## Features

- **Data Fetching:** Fetches top tracks from the Spotify API.
- **Analysis Tools:** Processes and analyzes the fetched data.
- **Visualization Support:** Provides an interface for further visualization or analysis.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/milanbhakta/DSI_SpotifyAPI.git
   ```
2. **Navigate to the package directory:**
   ```bash
   cd DSI_SpotifyAPI
   ``` 
3. **Install the package using pip:**
   ```bash
   pip install .
   ``` 
4. **OR Directly Install**
   ```bash
    !pip install https://github.com/milanbhakta/DSI_SpotifyAPI.git
   ```

## Usage
from spotify_package import Analysis

analysis_obj = Analysis('config.yml')
analysis_obj.load_data()

analysis_output = compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()

## Configuration

To use this package, create a .env file in the root directory with your Spotify API credentials:

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

## Testing
Ensure tests pass using pytest:
```bash
pytest
```

## Contribution Guidelines
We welcome contributions! To contribute to this project:

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).
3. Make changes and commit them (git commit -m 'Add feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

## Dependencies
* requests - HTTP library for making API requests.
* python-dotenv - Library for loading environment variables from .env file.
* pytest - Testing framework.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For any questions or support, please reach out via email or open an issue.