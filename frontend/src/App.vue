<script setup lang="ts">
import Header from './partials/Header.vue'
import Footer from './partials/Footer.vue'
</script>

<template>

  <div class="drawer drawer-mobile">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col items-center justify-center">
      <Header/>
      <div class="flex justify-center items-center h-screen">
        <div class="space-x-4">
          <h1 class="text-3xl mb-4 text-purple-500">
            How to Install Tailwind Daisyui In Vue 3
          </h1>
          <button class="btn">Button</button>
          <button class="btn btn-primary">Button</button>
          <button class="btn btn-secondary">Button</button>
          <button class="btn btn-accent">Button</button>
          <button class="btn btn-ghost">Button</button>
          <button class="btn btn-link">Button</button>
        </div>
      </div>
    </div>
    <div class="drawer-side">
      <label for="left-sidebar-drawer" class="drawer-overlay"></label>
      <ul class="menu  pt-2 w-80 bg-base-100 text-base-content">
        <li class="mb-2 font-semibold text-xl">

          <Link to="#"><img class="mask mask-squircle w-10" src="/images/asscat.png" alt="ASSCAT Logo"/>Smart Greenhouse</Link> </li>
        
        <div class="menu  pt-2 w-100 bg-base-100 text-base-content">
          <ul class="menu bg-base-100 w-100 p-2 rounded-box">
            <li>
              <a>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
                Item 2
              </a>
            </li>
            <li>
              <a>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                Item 1
              </a>
            </li>
            <li>
              <a>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                Item 3
              </a>
            </li>
          </ul>
    </div>
      </ul>

    </div>

  </div>
  <Footer/>




</template>

