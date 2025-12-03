<template>

  <p>{{ myProp.id }}</p>
  <p>{{ myProp.name }}</p>

</template>

<script setup>
  // my-props(케밥케이스) -> myProps(카멜케이스)
  defineProps({
    myProp: Object
  })
</script>

<style scoped>

</style>