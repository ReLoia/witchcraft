<script setup>

</script>

<template>
  <header>
    <div class="title">
    <span>witch</span>
    <span>CRAFT</span>
    <div id="underline">

    </div>
    </div>
    <div class="stats">
      <div class="digits">
        <span>0</span>
        <span>0</span>
        <span>0</span>
        <span>0</span>
      </div>
      <p>
        <span>sandwitches</span> <span>crafted</span>
      </p>
    </div>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script>

</script>

<style scoped>
  header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    padding-top: 20px;
    height: 90px;

    & > .title {
      text-align: center;
      font-size: 3.6rem;
      line-height: .75;
      width: fit-content;

      transform: scale(.6) rotate(-3deg);

      display: flex;
      flex-direction: column;
      letter-spacing: -4px;

      & > span {
        margin: 0;
        padding: 0;
        font-size: .9em;


        &:nth-child(2) {
          font-size: 1.1em;
          font-weight: bold;
          color: var(--primary);
        }
      }

      & > div#underline {
        width: 110%;
        height: 8px;

        transform: translate(-4%, 0);

        background-color: #D9D9D9;
        margin: 10px auto;
        border-radius: 24px;
      }
    }

    & > .stats {
      display: flex;
      flex-direction: column;
      align-items: center;

      transform: rotate(3deg);

      & > .digits {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;

        & > span {
          font-size: 3rem;
          line-height: .75;
          font-weight: bold;
        }
      }

      & > p {
        font-size: .85em;
        color: #D9D9D9;
      }
    }
  }

</style>
