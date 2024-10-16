from flask import Flask, render_template, jsonify
from backend.data_generator import TrafficDataGenerator
from backend.ai_agents import TrafficMonitoringAgent, SignalControlAgent, PublicCommunicationAgent, PredictiveAnalysisAgent
import logging

app = Flask(__name__)

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
    logger.info("Simulation requested")
    try:
        traffic_data = traffic_generator.generate_traffic_data()
        traffic_summary = monitoring_agent.analyze_traffic(traffic_data)
        signal_adjustments = signal_agent.adjust_signals(traffic_summary, traffic_data)
        public_alert = communication_agent.generate_alert(traffic_summary, signal_adjustments)
        traffic_prediction = predictive_agent.predict_traffic(traffic_data, traffic_summary)

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
