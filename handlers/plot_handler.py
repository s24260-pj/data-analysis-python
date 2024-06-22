from matplotlib import pyplot as plt

from command_types.chart_types import ChartTypes


class PlotHandler:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def generate_by_type(self, plot_type):
        if plot_type == ChartTypes.types["1"]:
            self.generate_age_distribution_players_plot()

            return

        if plot_type == ChartTypes.types["2"]:
            self.generate_market_value_vs_age_players_plot()
            return

        if plot_type == ChartTypes.types["3"]:
            self.generate_positional_distribution_players_plot()
            return

        if plot_type == ChartTypes.types["4"]:
            self.generate_top_10_clubs_by_count_players_plot()
            return

        raise ValueError(f"Unsupported action!")

    def generate_age_distribution_players_plot(self):
        plt.figure(figsize=(8, 6))
        plt.hist(self.data['Age'], bins=15, color='skyblue', edgecolor='black')
        plt.title('Age Distribution of Players')
        plt.xlabel('Age')
        plt.ylabel('Number of Players')
        plt.grid(True)
        plt.show()

    def generate_market_value_vs_age_players_plot(self):
        plt.figure(figsize=(10, 8))
        plt.scatter(self.data['Age'], self.data['MarketValue'], color='skyblue', alpha=0.6)
        plt.title('Market Value vs Age of Players')
        plt.xlabel('Age')
        plt.ylabel('Market Value')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def generate_positional_distribution_players_plot(self):
        plt.figure(figsize=(8, 6))
        position_counts = self.data['Position'].value_counts()
        plt.bar(position_counts.index, position_counts.values, color='skyblue')
        plt.title('Positional Distribution of Players')
        plt.xlabel('Position')
        plt.ylabel('Number of Players')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    def generate_top_10_clubs_by_count_players_plot(self):
        plt.figure(figsize=(10, 8))
        club_counts = self.data['Club'].value_counts().sort_values(ascending=False)[:10]
        plt.barh(club_counts.index, club_counts.values, color='lightgreen')
        plt.title('Top 10 Clubs by Number of Players')
        plt.xlabel('Number of Players')
        plt.ylabel('Club')
        plt.gca().invert_yaxis()
        plt.grid(axis='x')
        plt.tight_layout()
        plt.show()
