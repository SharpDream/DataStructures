class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.routes_dict = {}
        for From, To in self.edges:
            if From in self.routes_dict:
                self.routes_dict[From].append(To)
            else:
                self.routes_dict[From] = [To]

    def find_routes(self, From, To, path=[]):
        path = path + [From]

        if From == To:
            return [path]

        if From not in self.routes_dict:
            return []

        paths = []
        for node in self.routes_dict[From]:
            if node not in path:
                final_paths = self.find_routes(node, To, path)
                for p in final_paths:
                    paths.append(p)
        return paths

    def get_shortest(self, From, To, path=[]):
        path = path + [From]

        if From == To:
            return path

        if From not in self.routes_dict:
            return None

        shortest_path = None
        for node in self.routes_dict[From]:
            if node not in path:
                sp = self.get_shortest(node, To, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
