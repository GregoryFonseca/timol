---
title: 'Gala: A Python package for galactic dynamics'
tags:
  - Python
  - astronomy
  - dynamics
  - galactic dynamics
  - milky way
authors:
  - name: Gregory Fonseca
    orcid: 0000-0002-8041-0063
    affiliation: 1
  - name: Kyunghoon Han
    orcid: 0000-0001-7670-300X
    affiliation: 1
affiliations:
 - name: Department of Physics and Materials Science, University of Luxembourg
   index: 1
date: 24 March 2025
bibliography: paper.bib
---

# Summary

Molecular scientists today have access to a plethora of selection of molecular visualization tools. Many of these tools are readily available to the researchers worldwide, free of charge. However, as the computational demands for molecular simulations reached unprecedented levels today, more scientists are working directly on high-performance computing servers. This shift often complicates the process of connecting local visualization software to remote systems, frequently requiring the transfer of large molecular coordinate files for a quick preliminary check before generating publication-level images. Consequently, there exists a growing demand for a solution that enables direct molecular visualization on the serer via the terminal. Such a tool must be lightweight, user-friendly and customisable, featuring a graphical user interface that allows the users to quickly confirm that the molecular geometry or trajectory is physically accurate enough to proceed with subsequent steps--using either a mouse or keyboard according to their preference.

TIMOL (Terminal Interface MOLecular viewer) is a Python-based molecular visualization package that is easy-to-install, and satisfy the needs described above. The package allows the users to visualize their molecule directly on the terminal simply by installing the package only on the server-side once. TIMOL allows the users to easily check if their molecular coordinates or trajectories are physically, chemically or biologically correct directly from the server side. 

# Statement of need

Molecular visualization software is indispensable for today's molecular research. As machine learning-based projects gain prominence in the research scene, researchers are increasingly required to sift through numerous molecular coordinate files. These manual human-inspections are critical for assessing the quality and characteristics of datasets used either for training the models or for mid-project performance evaluations.

Additionally, non-machine learning projects benefit substantially from rapid visual checks. Computationally intensive, prolonged simulations often yield intermediate checkpoints comprising molecular coordinates or trajectories. Quick visualizations of these outputs allow researchers to efficiently verify whether their simulations adhere to the underlying physical principles, thereby minimizing the risk of error and reducing unncessary interruptions to their workflow.

Therefore, a lightweight terminal-based visualization tools are indispensable. Such tools would operate without substantial demands on computational resources or network bandwidth, making them ideally suited for high-performance computing environments. TIMOL exemplifies this approach by offering rapid, on-the-fly visualization that minimizes overhead and supports a smoother, more efficient workflow.

# The TIMOL package
