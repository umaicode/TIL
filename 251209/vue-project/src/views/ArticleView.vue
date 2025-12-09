<template>
  <div>
    <h1>게시판</h1>

    <RouterLink :to="{name: 'CreateView'}">
      [Create]
    </RouterLink>
    <!-- 전체 게시글 목록 -->
    <ArticleList />
  </div>
</template>

<script setup>

  import ArticleList from '@/components/ArticleList.vue';
  // 처음 화면에 들어왔을 때 실행
  import { onMounted } from 'vue';
  // 중앙저장소
  import { useArticleStore } from '@/stores/articles';

  const store = useArticleStore()

  // 화면 들어오자마자 전체 게시글 조회하겠다.
  onMounted(() => {
    store.getArticles()
  })

</script>

<style>

</style>
