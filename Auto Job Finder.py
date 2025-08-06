import streamlit as st
import requests

st.set_page_config(page_title="Auto Job Finder Demo", layout="centered")
st.title("🔍 Auto Job Finder Demo")

# Step 1: Enter Preferences
st.header("Step 1: Job Preferences")
job_title = st.text_input("Enter Job Title (e.g. Python Developer)")
preferred_location = st.selectbox(
    "Preferred Company Location",
    ["United States", "United Kingdom", "Canada", "Germany", "India", "Pakistan", "Australia", "Other"]
)
job_type = st.selectbox(
    "Preferred Job Type",
    ["Full-time", "Part-time", "Contract", "Internship", "Remote"]
)

# Function: fetch Remotive jobs (DEMO only using Remotive)
def fetch_remotive(title, location, jtype, limit=5):
    params = {"search": title, "limit": limit}
    resp = requests.get("https://remotive.com/api/remote-jobs", params=params)
    jobs = resp.json().get("jobs", [])
    return [
        {
            "title": job["title"],
            "company": job["company_name"],
            "location": job["candidate_required_location"],
            "url": job["url"],
            "type": job.get("job_type", "")
        }
        for job in jobs
    ]

if st.button("Search Jobs"):
    if not job_title:
        st.warning("Please enter a job title to search.")
    else:
        st.success(f"Showing jobs for '{job_title}' in {preferred_location}...")
        jobs = fetch_remotive(job_title, preferred_location, job_type)

        if not jobs:
            st.info("No job listings found.")
        else:
            st.subheader("Job Listings:")
            for job in jobs:
                st.markdown(f"**{job['title']}** — {job['company']}")
                st.markdown(f"*Location:* {job['location']} — *Type:* {job['type'] or 'N/A'}")
                st.markdown(f"[View Job Posting]({job['url']})")
                st.markdown("---")

st.markdown("---")
st.caption("Demo version – Get the full version with resume support & auto-apply on [Gumroad](https://janjua288.gumroad.com/l/hbvua)")
