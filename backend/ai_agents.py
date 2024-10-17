import google.generativeai as genai
import random
from datetime import datetime

# Configure Google Generative AI
GENAI_API_KEY = "KEY HERE"
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

        Provide a concise yet insightful analysis including:
        1. What the data reveals about current city traffic dynamics (1-2 sentences)
        2. Identify unexpected traffic hotspots or anomalies (1 sentence per hotspot)
        3. Compare the varying traffic flows between intersections, focusing on potential issues (1-2 sentences)
        4. Suggest a tactical traffic management action with an innovative edge

        Use sharp, precise language with a tone of authority.
        """
        
        response = model.generate_content(prompt)
        return response.text


class SignalControlAgent:
    def adjust_signals(self, traffic_summary, traffic_data):
        prompt = f"""
        Based on this traffic summary and data:

        Summary: {traffic_summary}
        Data: {traffic_data}

        Provide specific, actionable signal timing adjustments for each intersection. For each adjustment:
        1. Calculate a new green light duration based on the current traffic level and vehicle count.
        2. Specify any changes to the traffic flow pattern (e.g., lane prioritization, turn restrictions).
        3. Briefly explain the expected impact of these changes.

        Use the following guidelines for green light duration:
        - Low traffic: 30-45 seconds
        - Medium traffic: 45-60 seconds
        - High traffic: 60-90 seconds

        Adjust these base times according to the specific vehicle count and average speed.

        Format the response as follows for each intersection:
        - Intersection Name:
          Action: [Specific signal timing change and traffic flow adjustment]
          Expected Impact: [Brief explanation of the expected result]

        Focus on data-driven, quantitative adjustments that directly address the current traffic situation.
        """
        
        response = model.generate_content(prompt)
        return response.text


class PublicCommunicationAgent:
    def generate_alert(self, traffic_summary, signal_adjustments):
        current_time = datetime.now().strftime("%I:%M %p")
        
        prompt = f"""
        Create an eye-catching public traffic alert based on this information:

        Traffic Summary: {traffic_summary}
        Signal Adjustments: {signal_adjustments}
        Current Time: {current_time}

        The alert should:
        1. Start with "🚨 NYC Traffic Alert - [Current Time]:"
        2. Urgently highlight congestion areas, using clear visual language (e.g., 🚗🚗🚗)
        3. Summarize critical signal adjustments in a way that sounds innovative
        4. Provide engaging advice for commuters to think creatively about their route options.

        The tone should be lively, urgent, but reassuring and keep it under 50 words
        """
        
        response = model.generate_content(prompt)
        return response.text


class PredictiveAnalysisAgent:
    def predict_traffic(self, traffic_data, traffic_summary):
        prompt = f"""
        Based on the current traffic data and summary:

        Data: {traffic_data}
        Summary: {traffic_summary}

        Predict traffic patterns in the next 1-2 hours. 
        - Highlight expected increases in congestion with precision.
        - Identify potential opportunities for reducing traffic.
        - Reference potential influences (e.g., events, rush hours) with confidence.

        Keep the tone confident and forward-looking, under 100 words.
        """
        
        response = model.generate_content(prompt)
        return response.text
