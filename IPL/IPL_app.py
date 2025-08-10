import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style
sns.set(style="darkgrid")

# Title
st.title("IPL Cricket EDA Dashboard")

# Upload datasets
st.sidebar.header("Upload Datasets")
Matches_file = st.sidebar.file_uploader("Upload Matches.csv", type=["csv"])
Deliveries_file = st.sidebar.file_uploader("Upload Deliveries.csv", type=["csv"])

# Fix: Changed variable names in the if condition to match the defined variables
if Matches_file is not None and Deliveries_file is not None:
    Matches = pd.read_csv(Matches_file)
    Deliveries = pd.read_csv(Deliveries_file)

    # Clean matches data
    Matches['winner'].fillna('No Result', inplace=True)
    if 'umpire3' in Matches.columns:
        Matches.drop(['umpire3'], axis=1, inplace=True)

    st.sidebar.success("Datasets loaded successfully!")

    # Tabs for navigation
    tab1, tab2, tab3, tab4 = st.tabs(["Team Wins", " Toss Analysis", "Player Stats", " Season Insights"])

    with tab1:
        st.subheader("Most Matches Won by Teams")
        wins = Matches['winner'].value_counts()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=wins.index, y=wins.values, hue=wins.index, palette="viridis", dodge=False, legend=False, ax=ax)
        plt.xticks(rotation=45)
        plt.ylabel("Total Wins")
        plt.xlabel("Team")
        plt.tight_layout()
        st.pyplot(fig)

        if 'win_by_runs' in Matches.columns:
            st.subheader("Win by Runs Distribution")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            sns.histplot(Matches['win_by_runs'], bins=30, kde=True, color='orange', ax=ax2)
            plt.tight_layout()
            st.pyplot(fig2)

        if 'win_by_wickets' in Matches.columns:
            st.subheader("Win by Wickets Distribution")
            fig3, ax3 = plt.subplots(figsize=(10, 5))
            sns.histplot(Matches['win_by_wickets'], bins=30, kde=True, color='purple', ax=ax3)
            plt.tight_layout()
            st.pyplot(fig3)

    with tab2:
        st.subheader("Toss Impact Analysis")
        toss_match_win = Matches[Matches['toss_winner'] == Matches['winner']]
        # Fix: Changed variable name to Matches
        toss_win_percent = len(toss_match_win) / len(Matches) * 100
        st.metric("Toss Winner also won match (%)", f"{toss_win_percent:.2f}%")

        if 'toss_decision' in Matches.columns:
            st.subheader("Toss Decision Trends")
            fig4, ax4 = plt.subplots(figsize=(8, 5))
            sns.countplot(data=Matches, x='toss_decision', hue='toss_decision', ax=ax4, legend=False)
            plt.xticks(rotation=0)
            plt.tight_layout()
            st.pyplot(fig4)

    with tab3:
        st.subheader("Top 10 Run Scorers")
        if 'batsman' in Deliveries.columns and 'batsman_runs' in Deliveries.columns:
            top_scorers = Deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
            fig5, ax5 = plt.subplots(figsize=(10, 5))
            sns.barplot(x=top_scorers.index, y=top_scorers.values, palette="crest", hue=top_scorers.index, legend=False, ax=ax5)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig5)

        st.subheader("Top 10 Wicket Takers")
        if 'bowler' in Deliveries.columns and 'dismissal_kind' in Deliveries.columns:
            dismissals = Deliveries[Deliveries['dismissal_kind'].notnull()]
            top_wickets = dismissals.groupby('bowler').size().sort_values(ascending=False).head(10)
            fig6, ax6 = plt.subplots(figsize=(10, 5))
            sns.barplot(x=top_wickets.index, y=top_wickets.values, palette="rocket", hue=top_wickets.index, legend=False, ax=ax6)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig6)

    with tab4:
        st.subheader("Matches Played Per Season")
        if 'season' in Matches.columns:
            season_count = Matches['season'].value_counts().sort_index()
            fig7, ax7 = plt.subplots(figsize=(10, 5))
            sns.barplot(x=season_count.index, y=season_count.values, palette="mako", hue=season_count.index, legend=False, ax=ax7)
            plt.tight_layout()
            st.pyplot(fig7)

else:
    st.info("Please upload both Matches.csv and Deliveries.csv files from the IPL Kaggle dataset.")
