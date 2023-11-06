Na versão RLinWiFi-Decentralized-v14-30-station
o que foi feito foi o seguinte:

- Nova forma de carcular a Pcol = média das pcols de todas as estações
- adicionei ao construtor do agente (Class Agent) para criar instancias de agentes independentes
stationNum

class Agent:
    """Interacts with and learns from the environment."""
    TYPE = "discrete"
    NAME = "DQN"

    def __del__(self):
        tf.reset_default_graph()

    def __init__(self, network, state_size, action_size, stationNum=5, config=Config(), seed=42, save=True, save_loc='models/', save_every=2, checkpoint_file=None):
    

no notebook:
for i in range(agent_count):
    config = Config(buffer_size=3*steps_per_ep*threads_no, batch_size=32, gamma=0.7, tau=1e-3, lr=lr, update_every=1)
    agent = Agent(QNetworkTf, history_length, action_size=7, stationNum=i, config=config)
    agent.set_epsilon(0.9, 0.001, EPISODE_COUNT-2)
    agents.append(agent)
