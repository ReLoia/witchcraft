<script setup>
import Sandwitch from './SandwitchText.vue'
import '@jamescoyle/svg-icon'
import { mdiCartPlus, mdiDelete } from "@mdi/js";
import { reactive } from 'vue'

const ingredients = reactive([
  {
    name: "Ingredient",
    amount: 1,
    src: "https://via.placeholder.com/150"
  }
])

function addIngredient() {
  ingredients.push({
    name: "Ingredient",
    amount: 1,
    src: "https://via.placeholder.com/150"
  })
}

function removeIngredient(element) {
  const index = ingredients.indexOf(element)
  if (index > -1) {
    ingredients.splice(index, 1)
  }
}
</script>

<template>
  <h1>Craft your <Sandwitch /></h1>
  <div class="content">
    <div class="ingredients">
      <span>ingredients</span>
      <ul>
        <li v-for="ingredient in ingredients">
          <template v-for="i in ingredient.amount">
            <button @click="removeIngredient(ingredient)"> <svg-icon type="mdi" :path="mdiDelete" /> </button>
            <img :src="ingredient.src" alt="Could not load image" />
            <span>
              {{ ingredient.name }}
            </span>
<!--            remove button -->
          </template>
        </li>
      </ul>
      <button>
        <svg-icon type="mdi" :path="mdiCartPlus" />
      </button>
    </div>
  </div>
</template>

<style scoped>
h1 {
  margin-top: -4.8rem;
  font-size: 4.3rem;
  line-height: .75;
  font-weight: 400;
  letter-spacing: -4px;
}

div.content {
  display: flex;
  flex-direction: row;
  align-items: center;

  width: 100%;
  margin-top: 100px;

  & > .ingredients {
    width: 260px;
    border-radius: 24px;

    background: #000;
    box-shadow: -10px 14px 0 rgba(217, 217, 217, 0.8);

    position: relative;

    & > span {
      color: var(--secondary);
      font-size: 1.2rem;
      font-weight: bold;

      position: relative;
      top: -1rem;
      letter-spacing: 2px;

      left: 25%;
      transform: translateX(-50%);
    }

    & > ul {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 0;

      min-height: 500px;

      & > li {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 10px;
        position: relative;

        & > img {
          width: 100px;
          height: 100px;
        }

        & > span {
          color: var(--primary);
          font-size: .9rem;
          font-weight: bold;
          position: relative;
          top: -.7rem;
        }

        & > button {
          opacity: 0;
          pointer-events: none;

          color: var(--primary);
          scale: .8;

          cursor: pointer;

          background: none;
          border: none;
          padding: 0;

          position: absolute;
          top: -10px;
          right: -10px;

          transition: all .3s;

          background: var(--background);
          width: 34px;
          height: 34px;
          border-radius: 50%;
          line-height: 44px;
        }
        &:hover > button {
          pointer-events: all;
          opacity: 1;
        }
      }
    }

    & > button {
      color: var(--secondary);
      scale: 1.4;

      position: absolute;
      bottom: 14px;
      right: 14px;

      border: none;
      padding: 0;

      width: 32px;
      height: 32px;
      line-height: 46px;
    }

  }

}

</style>