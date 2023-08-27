import streamlit as st

# Function to display evidence in the resizable sidebar
def show_evidence(img_list):
    with st.sidebar:
        st.title("Evidence Data")

        # Inject custom JavaScript to make the sidebar resizable
        st.markdown(
            """
            <style>
            .resizable-sidebar {
                overflow: auto;
                resize: horizontal;
            }
            </style>
            <script>
            const sidebar = document.querySelector(".resizable-sidebar");
            const resizer = document.createElement("div");
            resizer.className = "resizer";
            sidebar.appendChild(resizer);

            resizer.addEventListener("mousedown", (e) => {
                e.preventDefault();
                const startX = e.clientX;
                const sidebarWidth = parseInt(getComputedStyle(sidebar).width, 10);

                document.documentElement.addEventListener("mousemove", onMouseMove);
                document.documentElement.addEventListener("mouseup", onMouseUp);

                function onMouseMove(e) {
                    const offsetX = e.clientX - startX;
                    sidebar.style.width = sidebarWidth + offsetX + "px";
                }

                function onMouseUp() {
                    document.documentElement.removeEventListener("mousemove", onMouseMove);
                    document.documentElement.removeEventListener("mouseup", onMouseUp);
                }
            });
            </script>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Display Evidence"):
            for i, img_path in enumerate(img_list):
                with st.sidebar:
                    st.image(img_path, caption=f"Evidence_{i+1}", use_column_width=True)
            st.session_state["evidence"] = True
        
        if st.button("Log out"):
            st.session_state.clear()
            st.cache_data.clear()
            st.experimental_rerun()

