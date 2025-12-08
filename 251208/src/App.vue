<template>
  <h1>오늘의 할 일</h1>

  <h2>완료된 할 일의 개수 : {{ store.doneTodoCount }}</h2>

  <!-- 할 일 목록 -->
  <TodoList />
  <!-- 할 일 생성 -->
  <TodoForm />
</template>

<script setup>
  // 중앙저장소 (stores의 counter.js) 가져오기
  import { useCounterStore } from './stores/counter';

  import TodoForm from '@/components/TodoForm.vue';
  import TodoList from '@/components/TodoList.vue';

  const store = useCounterStore
</script>

<style scoped>

</style>