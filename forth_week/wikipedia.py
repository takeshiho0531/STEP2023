import sys
from collections import deque


class Wikipedia:
    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):
        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}  # IDとtitleのマッチング

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}  # グラフのデータ構造

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()

    def get_id_from_title(self, title):
        for key, val in self.titles.items():
            if val == title:
                return key

    # Find the longest titles. This is not related to a graph algorithm at all
    # though :)
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()

    # Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()

    def BFS(self, start, goal):
        print(self.links)
        d = deque()
        start = self.get_id_from_title(start)
        goal = self.get_id_from_title(goal)
        d.append(start)
        visited = {}
        visited[start] = True

        while len(d) != 0:
            node = d.pop()
            if node == goal:
                return visited
            for child in self.links[node]:
                if not child in visited:
                    d.append(child)
                    visited[child] = node
        return "not found"

    # Find the shortest path.
    # |start|: The title of the start page.
    # |goal|: The title of the goal page.
    def find_shortest_path(self, start, goal):
        assert self.BFS(start, goal) != "not found"
        visited_dict = self.BFS(start, goal)
        start_id = self.get_id_from_title(start)
        goal_id = self.get_id_from_title(goal)
        node_id = goal_id
        path = []
        path.append(goal_id)

        while node_id != start_id:
            last_node_id = visited_dict[node_id]

            if last_node_id == start_id:
                path.append(last_node_id)
                path_title = []
                for i in range(len(path)):
                    node_title = self.titles[path[i]]
                    path_title.append(node_title)
                path_title.reverse()
                print(path_title)
                return
            if last_node_id != start_id:
                path.append(last_node_id)
                node_id = last_node_id

    def is_approximately_equal(self, list1, list2, threshold):
        if len(list1) != len(list2):
            return False

        for i in range(len(list1)):
            diff = abs(list1[i] - list2[i])
            if diff > threshold:
                return False

        return True

    def calculate_page_ranks(self):
        nodes_list = list(self.links.keys())
        page_ranks_dict = {}
        for node in nodes_list:
            page_ranks_dict[node] = 1
        update_log = []

        index = 0
        while (index == 0 or index == 1) or (
            self.is_approximately_equal(
                update_log[index - 1], update_log[index - 2], 0.01
            )
            == False
        ):
            for i in range(len(nodes_list)):
                node = nodes_list[i]
                child_num = len(self.links[node])
                # 隣接ページ self.links[nodes]
                for child in self.links[node]:
                    page_ranks_dict[child] += page_ranks_dict[node] * 0.85 / child_num
                page_ranks_dict[node] = page_ranks_dict[node] * 0.15
            update_log.append(list(page_ranks_dict.values()))
            index += 1
            print(sum(list(page_ranks_dict.values())))
            print(page_ranks_dict.values())
            continue
        else:
            print(page_ranks_dict)
            return page_ranks_dict

    # Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):
        page_ranks_dict = self.calculate_page_ranks()
        sorted_list = sorted(page_ranks_dict.items(), key=lambda x: x[1])
        top10_list = sorted_list[:10]

        title_top10_list = []
        for i in range(len(top10_list)):
            node_id = top10_list[i][0]
            node_title = self.titles[node_id]
            title_top10_list.append((node_title, top10_list[i][1]))

        top10_dict = {key: value for key, value in title_top10_list}
        print(top10_dict)

    # Do something more interesting!!
    def find_something_more_interesting(self):
        # ------------------------#
        # Write your code here!  #
        # ------------------------#
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    wikipedia.find_longest_titles()
    # wikipedia.find_most_linked_pages()
    # wikipedia.find_shortest_path("渋谷", "パレートの法則")
    # wikipedia.BFS("A", "C")
    # wikipedia.find_shortest_path("A", "C")
    wikipedia.find_most_popular_pages()
