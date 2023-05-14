<template>
  <div class="drawer-side">
    <label for="left-sidebar-drawer" class="drawer-overlay"></label>
    <ul class="menu  pt-2 w-80 bg-base-100 text-base-content bg-base-200 w-80">
      <li class="mb-2 font-semibold text-xl">

        <Link to="#"><img class="mask mask-squircle w-10" src="/images/asscat.png" alt="ASSCAT Logo"/>Smart Greenhouse
        </Link>
      </li>
      <Menu/>

    </ul>

  </div>
</template>

<script setup lang="ts">
import Menu from './Menu.vue'

</script>

<style scoped>

</style>