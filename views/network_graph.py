from pyvis.network import Network
import tempfile

def build_network(df):

    net = Network(
        height="700px",
        width="100%",
        bgcolor="#061826",
        font_color="white"
    )

    suspects = set()
    victims = set()
    stations = set()

    for _, row in df.iterrows():

        suspect = row["Suspect_Name"]
        victim = row["Victim_Name"]
        station = row["Police_Station"]

        if suspect not in suspects:
            net.add_node(
                suspect,
                label=suspect,
                color="red",
                title="Suspect"
            )
            suspects.add(suspect)

        if victim not in victims:
            net.add_node(
                victim,
                label=victim,
                color="orange",
                title="Victim"
            )
            victims.add(victim)

        if station not in stations:
            net.add_node(
                station,
                label=station,
                color="cyan",
                title="Police Station"
            )
            stations.add(station)

        net.add_edge(suspect, victim)

        net.add_edge(victim, station)

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".html")

    net.save_graph(temp.name)

    return temp.name