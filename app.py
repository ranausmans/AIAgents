from flask import Flask, render_template, jsonify, request
from backend.data_generator import TrafficDataGenerator
from backend.ai_agents import TrafficMonitoringAgent, SignalControlAgent, PublicCommunicationAgent, PredictiveAnalysisAgent
import logging

app = Flask(__name__)

# Add this line to handle the /aitraffic/ prefix
app.config['APPLICATION_ROOT'] = '/aitraffic'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

traffic_generator = TrafficDataGenerator()
monitoring_agent = TrafficMonitoringAgent()
signal_agent = SignalControlAgent()
communication_agent = PublicCommunicationAgent()
predictive_agent = PredictiveAnalysisAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # Add some logging here
    app.logger.info(f"Received simulate request. Headers: {request.headers}")
    app.logger.info(f"Request data: {request.get_data()}")
    
    logger.info("Simulation requested")
    try:
        traffic_data = traffic_generator.generate_traffic_data()
        logger.info(f"Generated traffic data: {traffic_data}")

        traffic_summary = monitoring_agent.analyze_traffic(traffic_data)
        logger.info(f"Traffic summary: {traffic_summary}")

        signal_adjustments = signal_agent.adjust_signals(traffic_summary, traffic_data)
        logger.info(f"Signal adjustments: {signal_adjustments}")

        public_alert = communication_agent.generate_alert(traffic_summary, signal_adjustments)
        logger.info(f"Public alert: {public_alert}")

        traffic_prediction = predictive_agent.predict_traffic(traffic_data, traffic_summary)
        logger.info(f"Traffic prediction: {traffic_prediction}")

        return jsonify({
            'traffic_data': traffic_data,
            'traffic_summary': traffic_summary,
            'signal_adjustments': signal_adjustments,
            'public_alert': public_alert,
            'traffic_prediction': traffic_prediction
        })
    except Exception as e:
        logger.error(f"Error in simulation: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting the application")
    app.run(debug=True, host='0.0.0.0', port=5004)
