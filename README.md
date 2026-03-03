# LaunchDarkly Dynamic Rec Engine

A production-grade demonstration of feature management and experimentation.

## Technical Choices
- **Singleton Wrapper:** Isolated the SDK into `ld_client.py` for better testability and maintenance.
- **Variation Detail:** Used `variation_detail` to expose the underlying reason for flag evaluation—useful for production observability.
- **Graceful Fallbacks:** All flag calls include a default value to ensure the app remains functional if the SDK is unreachable.
- **Experimentation:** Integrated `.track()` to feed real-time engagement data into the LD Experimentation engine.

## Instructions
1. `pip install -r requirements.txt`
2. Add your key to `.env`
3. Run `python app.py`
