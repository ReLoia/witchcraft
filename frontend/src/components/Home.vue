<script setup>
import {onMounted, reactive, ref} from 'vue'
import { useStore} from "vuex";
const store = useStore();

// TODO: load sandwitches from the server
const sandwitches = ref([]);

onMounted(async () => {
  const response = await fetch('/api/sandwitches');
  if (response.ok) {
    sandwitches.value = await response.json();
  }
})

</script>

<template>
  <h1>Recent SandWitches</h1>
  <router-link to="/craft">Craft yours</router-link>
  <div class="container">
    <div class="loading" v-if="sandwitches.length == 0">
      <span>There are no sandwitches yet</span>
    </div>
    <div v-else class="sandwitch" v-for="sandwitch in sandwitches">
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

  </div>
</template>

<style scoped>

h1 + a {
  margin-top: 1rem;
  font-weight: bold;
  font-size: 1.4rem;

  display: inline-block;
  position: relative;
  z-index: 1;

  --back-top: 53%;
  transition: margin-top .3s, margin-bottom .3s, top .3s;

  top: 0;

  &:hover {
    top: -.3rem;
    --back-top: 65%;
  }

  &:after {
    content: "";
    display: block;
    width: 80%;
    height: 40%;

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

  margin-top: 70px;
  width: 100%;

  gap: 40px;
  padding-inline: 40px;

  & > div.sandwitch {
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
}
</style>