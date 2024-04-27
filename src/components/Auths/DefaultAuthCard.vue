<script setup></script>

<template>
  <div
    class="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark"
  >
    <div class="flex flex-wrap items-center">
      <div class="w-full border-stroke dark:border-strokedark p-4">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
