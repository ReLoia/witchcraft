<script setup>
const props = defineProps(['sandwitch']);

const sandwitch = props.sandwitch;

</script>

<template>
<div class="sandwitch">
  <div class="info">
    <img :src="sandwitch.preview" alt="Could not load image" />
    <span>{{ sandwitch.name }}</span>
  </div>
  <div class="ingredients">
    <span>ingredients</span>
    <ul>
      <li v-for="ingredient in sandwitch.ingredients">
        <template v-for="i in ingredient.amount">
          <img :src="ingredient.src" alt="Could not load image" />
          <span>{{ ingredient.name }}</span>
        </template>
      </li>
    </ul>
  </div>
  <div class="likes">
    <span>likes</span>
    <span>{{ sandwitch.likes }}</span>
  </div>

</div>
</template>

<style scoped>
div.sandwitch {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 20px;

    background: #000;
    padding: 0 2rem;

    height: 110px;
    border-radius: 18px;

    box-sizing: border-box;

    width: 100%;

    & > div.info {
      display: flex;
      flex-direction: column;
      align-items: center;

      & > img {
        width: 120px;
        height: 120px;
        min-height: 120px;
        margin-top: -1.4rem;
      }

      & > span {
        color: var(--secondary);

        font-size: 1.3rem;
        font-weight: bold;
        margin-top: -1.24rem;
        margin-bottom: 1.24rem;

        display: inline-block;
      }
    }

    & > div.ingredients {
      width: 100%;

      & > span {
        color: var(--secondary);
        font-size: 1.1rem;
        font-weight: bold;

        position: relative;
        top: -.7rem;
        letter-spacing: 2px;
      }

      & > ul {
        display: flex;
        flex-direction: row;
        gap: 10px;
        padding-inline: 10px;

        & > li {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 5px;

          & > img {
            width: 80px;
            height: 80px;
          }

          & > span {
            color: var(--primary);
            font-size: .8rem;
            font-weight: bold;

            position: relative;
            top: -.8rem;
          }
        }
      }

    }

    & > div.likes {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      & > span:first-of-type {
        color: var(--secondary);
        line-height: 0;

        font-size: 1.1rem;
      }

      & > span:last-of-type {

        font-size: 1.7rem;
        font-weight: bold;
      }

    }

  }

</style>