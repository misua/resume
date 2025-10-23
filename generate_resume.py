#!/usr/bin/env python3
"""
ATS-Friendly Resume Generator
Creates a clean, professional PDF resume optimized for Applicant Tracking Systems
Two-column layout matching the provided template
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white

def create_resume():
    # Create PDF
    filename = "Charles_Pino_Resume.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Colors
    header_blue = HexColor('#29395E')
    
    # Header Section (Full Width, Dark Blue Background)
    c.setFillColor(header_blue)
    c.rect(0, height - 1.2*inch, width, 1.2*inch, fill=True, stroke=False)
    
    # Header Text (White)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(0.75*inch, height - 0.55*inch, "CHARLES M. PINO")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75*inch, height - 0.75*inch, "Site Reliability Engineer | DevOps Specialist")
    
    c.setFont("Helvetica", 9)
    c.drawString(0.75*inch, height - 0.95*inch, "☎ +639470318319")
    c.drawString(3.2*inch, height - 0.95*inch, "✉ biss.dakk@gmail.com")
    
    c.drawString(0.75*inch, height - 1.1*inch, "📍 Philippines")
    c.drawString(3.2*inch, height - 1.1*inch, "🔗 github.io/misua")
    
    # Reset to black for body
    c.setFillColor(black)
    
    # Starting Y position for content
    y = height - 1.5*inch
    left_margin = 0.75*inch
    left_column_width = 3.5*inch  # Width of left column
    right_column_x = 4.5*inch  # Start of right column
    
    # LEFT COLUMN
    
    # SUMMARY Section
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "SUMMARY")
    c.line(left_margin, y - 0.05*inch, left_margin + left_column_width, y - 0.05*inch)
    y -= 0.25*inch
    
    c.setFont("Helvetica", 10)
    summary_text = [
        "Seasoned Site Reliability Engineer with 10+ years of",
        "experience in cloud infrastructure, DevOps practices, and",
        "Kubernetes environments. Specialized in building scalable,",
        "resilient systems with strong focus on observability,",
        "GitOps, and security. Proven track record of optimizing",
        "infrastructure performance and implementing automation",
        "solutions across AWS, GCP, and Azure platforms."
    ]
    for line in summary_text:
        c.drawString(left_margin, y, line)
        y -= 0.16*inch
    
    y -= 0.2*inch
    
    # EDUCATION Section
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "EDUCATION")
    c.line(left_margin, y - 0.05*inch, left_margin + left_column_width, y - 0.05*inch)
    y -= 0.25*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, y, "B.S. Computer Science")
    c.setFont("Helvetica", 10)
    c.drawString(left_margin + 2.6*inch, y, "GPA")
    y -= 0.17*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, y, "AMA Computer University")
    c.setFont("Helvetica", 10)
    c.drawString(left_margin + 2.6*inch, y, "N/A")
    y -= 0.17*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(left_margin, y, "📅 Graduated    📍 Davao City, Philippines")
    y -= 0.25*inch
    
    # EXPERIENCE Section
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "EXPERIENCE")
    c.line(left_margin, y - 0.05*inch, left_margin + left_column_width, y - 0.05*inch)
    y -= 0.3*inch
    
    # Job 1: Ujet.cx
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "Site Reliability Engineer")
    y -= 0.16*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, y, "Ujet.cx")
    c.setFont("Helvetica", 9)
    c.drawString(left_margin + 0.5*inch, y, "📅 2023 - 2025    📍 Remote")
    y -= 0.17*inch
    
    c.setFont("Helvetica", 9)
    job1_bullets = [
        "• Designed and implemented cloud infrastructure (EKS,",
        "  GKE, Kubernetes) and CI/CD pipelines, reducing",
        "  customer deployment time by 40%",
        "• Integrated security controls (SAST, Snyk, Clair) and",
        "  APM, resulting in 30% faster incident detection",
        "• Developed infrastructure using Pulumi and Terraform",
        "  with Vault, achieving 95% IaC coverage"
    ]
    for bullet in job1_bullets:
        c.drawString(left_margin + 0.08*inch, y, bullet)
        y -= 0.13*inch
    y -= 0.2*inch
    
    # Job 2: Paack
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "Site Reliability Engineer")
    y -= 0.16*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, y, "Paack")
    c.setFont("Helvetica", 9)
    c.drawString(left_margin + 0.5*inch, y, "📅 2021 - 2023    📍 Remote")
    y -= 0.17*inch
    
    c.setFont("Helvetica", 9)
    job2_bullets = [
        "• Ensured high availability for platform serving 20+",
        "  million monthly users on GCP with 99.9% uptime",
        "• Enhanced system performance with Grafana,",
        "  Prometheus, Loki, reducing latency by 35%",
        "• Implemented GitOps with ArgoCD and Flagger,",
        "  decreasing deployment failures by 60%"
    ]
    for bullet in job2_bullets:
        c.drawString(left_margin + 0.08*inch, y, bullet)
        y -= 0.13*inch
    y -= 0.2*inch
    
    # Job 3: Orecx LLC - DevOps
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "DevOps Engineer")
    y -= 0.16*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, y, "Orecx LLC")
    c.setFont("Helvetica", 9)
    c.drawString(left_margin + 0.75*inch, y, "📅 2016 - 2020    📍 Remote")
    y -= 0.17*inch
    
    c.setFont("Helvetica", 9)
    job3_bullets = [
        "• Implemented CI/CD pipelines with GitLab CI/CD and",
        "  Kubernetes, resulting in 75% reduction in",
        "  deployment time and 99.9% success rate",
        "• Managed IaC scripts using Terraform for hundreds",
        "  of production environments",
        "• Led incident response team, reducing P1 incidents",
        "  by 40%"
    ]
    for bullet in job3_bullets:
        c.drawString(left_margin + 0.08*inch, y, bullet)
        y -= 0.13*inch
    y -= 0.2*inch
    
    # Job 4: Orecx LLC - Linux Support
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin, y, "Linux Support Engineer")
    y -= 0.16*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, y, "Orecx LLC")
    c.setFont("Helvetica", 9)
    c.drawString(left_margin + 0.75*inch, y, "📅 2010 - 2016    📍 Remote")
    y -= 0.17*inch
    
    c.setFont("Helvetica", 9)
    job4_bullets = [
        "• Conducted capacity planning and disaster recovery",
        "  testing, achieving 99.5% uptime",
        "• Optimized Linux server configurations, resulting in",
        "  20% reduction in latency",
        "• Developed disaster recovery plans, reducing",
        "  downtime from 4 hours to 30 minutes"
    ]
    for bullet in job4_bullets:
        c.drawString(left_margin + 0.08*inch, y, bullet)
        y -= 0.13*inch
    
    # RIGHT COLUMN
    y_right = height - 1.5*inch
    
    # SKILLS Section
    c.setFont("Helvetica-Bold", 11)
    c.drawString(right_column_x, y_right, "SKILLS")
    c.line(right_column_x, y_right - 0.05*inch, width - 0.75*inch, y_right - 0.05*inch)
    y_right -= 0.28*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Programming Skills")
    y_right -= 0.19*inch
    
    c.setFont("Helvetica", 9)
    # Skills as boxes
    skills_prog = ["Golang", "Python", "Bash"]
    x_skill = right_column_x
    for skill in skills_prog:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Databases & Cloud services")
    y_right -= 0.19*inch
    
    c.setFont("Helvetica", 9)
    skills_db = ["PostgreSQL", "MySQL", "Redis"]
    x_skill = right_column_x
    for skill in skills_db:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.22*inch
    
    skills_cloud = ["Pub/Sub", "AWS", "GCP", "Azure"]
    x_skill = right_column_x
    for skill in skills_cloud:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Tools")
    y_right -= 0.19*inch
    
    c.setFont("Helvetica", 9)
    skills_tools = ["Kubernetes", "Docker", "Terraform"]
    x_skill = right_column_x
    for skill in skills_tools:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.22*inch
    
    skills_tools2 = ["Pulumi", "Ansible"]
    x_skill = right_column_x
    for skill in skills_tools2:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Development")
    y_right -= 0.19*inch
    
    c.setFont("Helvetica", 9)
    skills_dev = ["GitHub Actions", "Azure Pipelines"]
    x_skill = right_column_x
    for skill in skills_dev:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.22*inch
    
    skills_dev2 = ["GitLab CI", "Argo CD", "Argo Rollouts"]
    x_skill = right_column_x
    for skill in skills_dev2:
        c.rect(x_skill, y_right - 0.02*inch, len(skill)*0.06*inch + 0.15*inch, 0.15*inch, fill=False, stroke=True)
        c.drawString(x_skill + 0.08*inch, y_right + 0.02*inch, skill)
        x_skill += len(skill)*0.06*inch + 0.25*inch
    y_right -= 0.35*inch
    
    # CERTIFICATION Section
    c.setFont("Helvetica-Bold", 11)
    c.drawString(right_column_x, y_right, "CERTIFICATION")
    c.line(right_column_x, y_right - 0.05*inch, width - 0.75*inch, y_right - 0.05*inch)
    y_right -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Coursera DevOps Professional")
    y_right -= 0.15*inch
    c.setFont("Helvetica", 9)
    c.drawString(right_column_x, y_right, "Coursera, 2023")
    y_right -= 0.25*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Tigera Certified Kubernetes")
    y_right -= 0.15*inch
    c.drawString(right_column_x, y_right, "Security Specialist")
    y_right -= 0.15*inch
    c.setFont("Helvetica", 9)
    c.drawString(right_column_x, y_right, "Tigera Academy, 2023")
    y_right -= 0.25*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "Certified Kubernetes Administrator")
    y_right -= 0.15*inch
    c.setFont("Helvetica", 9)
    c.drawString(right_column_x, y_right, "KodeKloud, 2022")
    y_right -= 0.35*inch
    
    # STRENGTHS Section
    c.setFont("Helvetica-Bold", 11)
    c.drawString(right_column_x, y_right, "STRENGTHS")
    c.line(right_column_x, y_right - 0.05*inch, width - 0.75*inch, y_right - 0.05*inch)
    y_right -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "💬 Communication")
    y_right -= 0.18*inch
    c.setFont("Helvetica", 9)
    comm_text = [
        "Open-minded, outgoing and patient in",
        "conversations with others. Strong",
        "collaboration skills across distributed teams."
    ]
    for line in comm_text:
        c.drawString(right_column_x, y_right, line)
        y_right -= 0.15*inch
    y_right -= 0.15*inch
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_column_x, y_right, "⭐ Problem Solving & Technical")
    y_right -= 0.15*inch
    c.drawString(right_column_x, y_right, "Excellence")
    y_right -= 0.18*inch
    c.setFont("Helvetica", 9)
    tech_text = [
        "Proven ability to optimize complex systems,",
        "reduce latency, and implement scalable",
        "solutions. Strong focus on automation,",
        "observability, and security best practices."
    ]
    for line in tech_text:
        c.drawString(right_column_x, y_right, line)
        y_right -= 0.15*inch
    
    c.save()
    print("✓ Resume PDF generated successfully: Charles_Pino_Resume.pdf")

if __name__ == "__main__":
    create_resume()
