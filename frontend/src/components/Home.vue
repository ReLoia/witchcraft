<script setup>

</script>

<template>
  <h1>Recent SandWitches</h1>
  <a href="">Craft yours</a>
  <div class="container">
    <div class="sandwitch">
      <img src="" alt="">
      <h2>{{ 'name' }}</h2>
    </div>
  </div>
</template>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>

<style scoped>
  h1 {
    margin-top: -4.8rem;
    font-size: 4.2rem;
    line-height: .75;
    font-weight: 500;
    letter-spacing: -4px;
  }

  h1 + a {
    margin-top: 1rem;
    font-weight: bold;
    font-size: 1.6rem;

    display: inline-block;
    position: relative;
    z-index: 1;

    --back-top: 30%;
    transition: margin-top .3s;

    &:hover {
      margin-top: .7rem;
      --back-top: 42%;
    }

    &:after {
      content: "";
      display: block;
      width: 90%;
      height: 70%;

      transition: top .3s;

      position: absolute;
      top: var(--back-top);
      left: 50%;
      transform: translateX(-50%);
      z-index: -1;

      border-radius: 50px;

      background: black;
    }
  }

  div.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>