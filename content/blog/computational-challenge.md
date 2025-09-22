+++
title = 'Can you solve this computational challenge?'
date = "2025-09-21"
description = "A computational challenge involving the Doppler effect in an audio recording of a passing Formula 1 car."
tags = ["physics", "computational science", "Doppler effect", "audio processing"]
[Params]
shortpath = "cc1"
bsky = "https://bsky.app/profile/tovrstra.bsky.social/post/3lzelqdlgic2s"
+++

Are you looking for a challenge for your BSc or undergraduate students in a computational science/physics course?
This one is easy to explain, but slightly more involved to solve,
and anyone solving it will learn something and have fun along the way.

## The challenge

You can clearly recognize the [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect)
in the following audio recording of a Formula 1 car:

🔊 [formula1.wav](/formula1.wav)

Estimate the following quantities by analyzing this recording:

- The speed of the car.
- The closest distance between the car and the microphone.
- The time at which the car is closest to the microphone.
- The frequency at which the car engine is running.

You can assume that the car drives at a constant velocity on a straight line, and that the microphone is stationary.

Good luck!

## Background info

This problem was originally a question in the retake exam in the summer of 2025 of the course [Python for Scientists](https://studiekiezer.ugent.be/2025/studiefiche/en/C004212) for the second bachelors in [Physics and Astronomy](https://studiekiezer.ugent.be/2025/bachelor-of-science-in-physics-and-astronomy) at [Ghent University](https://www.ugent.be/).
At the exam, we provided the same audio file in NPY format and broke the problem down into smaller questions.

The audio was extracted from an enthusiastic recording of a Formula 1 race (Silverstone 2017) posted on YouTube.
For those who cannot get enough of the Doppler effect, you can enjoy [the full recording here](https://www.youtube.com/watch?v=3w8_WzQzfTY).

## Check your results

You should find approximately that:

- the car is driving 68 m/s (245 km/h),
- the closest distance between the car and the microphone is 15 m,
- the time at which the car is closest to the microphone is at 1.6 s in the recording, and
- the car engine runs at a frequency of 337 Hz (20220 rpm).

## Share your solution

If you've solved the challenge and have posted your implementation on-line,
e.g. Jupyter Notebook on GitHub, please reply to my [bluesky post](https://bsky.app/profile/tovrstra.bsky.social/post/3lzelqdlgic2s) with a link to your solution.
I'm happy to take a look!
