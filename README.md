# LaunchDarkly Dynamic Recommendation Engine

This project is a mock e-commerce recommendation service designed to demonstrate how feature management and experimentation work in a live environment. I built it to show how a business can safely roll out new features to specific users and measure the results using data rather than guesswork.

## Technical Choices

* **Singleton Wrapper:** I moved the LaunchDarkly SDK logic into its own dedicated file called `ld_client.py`. This creates a single point of truth for the SDK initialization. By using a singleton pattern, the application avoids the overhead of creating new connections every time a flag needs to be checked, which is a standard best practice for performance in high-traffic applications.

* **Detailed Evaluation:** Instead of just requesting a simple true or false value, I used the `variation_detail` method. This allows the application to see the reasoning behind a decision, such as whether a user matched a specific target rule or fell through to the default setting. This level of detail is essential for debugging and provides better observability into how the rules engine is behaving.

* **Graceful Fallbacks:** I ensured that every flag request includes a hardcoded default value. If the server loses its internet connection or the SDK fails to initialize, the application will continue to run without crashing. It simply serves the standard user experience until the connection is restored.

* **Experimentation Loop:** I integrated the `.track()` function to send engagement data back to the LaunchDarkly dashboard. This bridges the gap between engineering and product goals. By tracking a mock "click" metric, we can compare how the premium algorithm performs against the standard one in real time.



## Instructions

1.  **Install dependencies:**
    Run the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment Variables:**
    Create a file named `.env` in the root directory and add your SDK key:
    ```text
    LD_SDK_KEY=your-actual-key-here
    ```

3.  **Execute the application:**
    Run the main script:
    ```bash
    python app.py
    ```

## Evaluation and Testing

I verify the project by running the script and comparing the output for two different user contexts. The first group, labeled as **beta-testers**, should trigger a specific targeting rule that serves the premium items. The second group, labeled as **standard-users**, should miss that rule and receive the standard items instead.

I also monitor the LaunchDarkly **Debugger** tab while the script runs. This confirms that evaluation events and custom click metrics are being successfully transmitted to the cloud. This end-to-end flow proves that the application can handle dynamic updates and record experimental data without requiring any manual code changes or redeployments.
