import streamlit as st



st.logo('12.png')

recommendations=st.Page(
    page="views/app1.py",
    title="MOVIE RECOMMENDATIONS",
    icon=":material/live_tv:"   
)
about=st.Page(
        page="views/about.py",
        title="ABOUT",
        icon=":material/person:"
)
movielist=st.Page(
        page="views/movie list.py",
        title="MOVIES",
        icon=":material/movie:"
)
imdb=st.Page(
        page="views/top imdb rated.py",
        title="IMDB",
        icon=":material/bar_chart:"
)
pg=st.navigation(pages=[recommendations,about,movielist,imdb])
pg.run()
