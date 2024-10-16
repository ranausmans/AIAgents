import google.generativeai as genai
import random
from datetime import datetime

# Configure Google Generative AI
GENAI_API_KEY = "AIzaSyDceI3mqdAoSIPkGpYgbttbuJ-YUwoLk3E"
genai.configure(api_key=GENAI_API_KEY)

# Set up the Generative AI model configuration
generation_config = {
    "temperature": 0.15,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

class TrafficMonitoringAgent:
    def analyze_traffic(self, traffic_data):
        prompt = f"""
        Analyze the following traffic data for 5 NYC intersections:

        {traffic_data}

        Provide a concise analysis including:
        1. Overall traffic situation summary (1-2 sentences)
        2. Identification of congestion hotspots, if any (1 sentence per hotspot)
        3. Brief comparison of traffic levels across intersections (1-2 sentences)
        4. One key suggestion for immediate traffic management action

        Format the analysis in short, clear paragraphs. Keep the entire analysis under 150 words.
        """
        
        response = model.generate_content(prompt)
        return response.text

class SignalControlAgent:
    def adjust_signals(self, traffic_summary, traffic_data):
        prompt = f"""
        Based on this traffic summary and data:

        Summary: {traffic_summary}
        Data: {traffic_data}

        Suggest specific signal timing adjustments for each intersection. For each adjustment, provide a brief explanation.
        Format the response as:

        1. Intersection Name:
           - Adjustment: [Specific adjustment]
           - Reason: [Brief explanation]

        Repeat this format for all intersections.
        """
        
        response = model.generate_content(prompt)
        return response.text

class PublicCommunicationAgent:
    def generate_alert(self, traffic_summary, signal_adjustments):
        current_time = datetime.now().strftime("%I:%M %p")
        
        prompt = f"""
        Create a public traffic alert based on this information:

        Traffic Summary: {traffic_summary}
        Signal Adjustments: {signal_adjustments}
        Current Time: {current_time}

        The alert should:
        1. Start with "NYC Traffic Alert - [Current Time]:"
        2. Highlight any high congestion areas (if any)
        3. Mention key signal adjustments
        4. Provide brief advice for commuters

        Keep the alert concise and under 100 words.
        """
        
        response = model.generate_content(prompt)
        return response.text

class PredictiveAnalysisAgent:
    def predict_traffic(self, traffic_data, traffic_summary):
        prompt = f"""
        Based on the current traffic data and summary:

        Data: {traffic_data}
        Summary: {traffic_summary}

        Provide a short-term traffic prediction for the next 1-2 hours. Include:
        1. Expected changes in traffic patterns
        2. Potential congestion points
        3. Any events or factors that might influence traffic

        Keep the prediction concise, under 100 words.
        """
        
        response = model.generate_content(prompt)
        return response.text
