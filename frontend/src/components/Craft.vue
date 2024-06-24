<script setup>
import Sandwitch from './SandwitchText.vue'
import '@jamescoyle/svg-icon'
import {mdiCartPlus, mdiDelete, mdiPlusCircle} from "@mdi/js";
import {reactive} from 'vue'

// INGREDIENTS

const ingredients = reactive([
  {
    name: "Ingredient",
    amount: 1,
    src: "https://via.placeholder.com/150"
  }
])

// TODO: make ingredients get loaded from backend

function addIngredient(ingredient) {
  ingredients.push(ingredient)
}

function removeIngredient(element) {
  const index = ingredients.indexOf(element)
  if (index > -1) {
    ingredients.splice(index, 1)
  }
}

// GENRES

// TODO: move ingredients to backend and make it load from backend
// TODO: also make ingredients editable from users (creating new ones)
const possibleGenres = reactive([
  "magical", "psychical", "metallic", "organic", "plastic", "wooden", "glass", "stone", "liquid", "gaseous", "solid", "hot", "cold", "frozen", "burning", "rotten", "fresh", "artificial", "natural", "synthetic", "alien", "human", "animal", "plant", "mineral", "chemical", "biological", "technological", "spiritual", "emotional", "physical", "mental", "abstract", "concrete", "tasteful", "tasteless", "smelly", "smell-less",
])

const sandWitch = reactive({
  name: "",
  description: "",
  genre: ["magical"]
})

function addGenre(genre) {
  sandWitch.genre.push(genre)
}

function removeGenre(genre) {
  const index = sandWitch.genre.indexOf(genre)
  if (index > -1) {
    sandWitch.genre.splice(index, 1)
  }
}


</script>

<template>
  <h1>Craft your
    <Sandwitch/>
  </h1>
  <div class="content">
    <div class="ingredients">
      <span>ingredients</span>
      <ul>
        <li v-for="ingredient in ingredients">
          <template v-for="i in ingredient.amount">
            <button @click="removeIngredient(ingredient)">
              <svg-icon type="mdi" :path="mdiDelete"/>
            </button>
            <img :src="ingredient.src" alt="Could not load image"/>
            <span>
              {{ ingredient.name }}
            </span>
          </template>
        </li>
      </ul>
      <button>
        <svg-icon type="mdi" :path="mdiCartPlus"/>
      </button>
    </div>
    <div class="craft">
      <div class="input">
        <label for="">name your
          <Sandwitch/>
        </label>
        <input type="text"/>
      </div>
      <!--   describe your sandwitch   -->
      <div class="input">
        <label for="">describe your
          <Sandwitch/>
        </label>
        <textarea name="" id="" cols="30" rows="10"></textarea>
      </div>
      <!--      what kind of sandwitch did you make, just a div because this will contain custom elements -->
      <div class="input">
        <label for="">what kind of
          <Sandwitch/>
          did you make</label>
        <div class="genres">
          <!--    display all genre in sandWitch element      -->
          <div class="genre" v-for="genre in sandWitch.genre">
            <span>{{ genre }}</span>
            <button @click="removeGenre(genre)">
              <svg-icon type="mdi" :path="mdiDelete"/>
            </button>
          </div>

          <button>
            <svg-icon type="mdi" :path="mdiPlusCircle"/>
          </button>
        </div>
      </div>
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
  justify-content: space-between;

  width: 100%;
  margin-top: 100px;

  gap: 100px;


  & > .ingredients {
    width: 280px;
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

  & > .craft {
    width: 90%;
    max-width: 760px;

    margin-top: -27px;

    & > .input {
      display: flex;
      flex-direction: column;
      gap: 10px;

      & > label {
        font-size: 1.3rem;
        letter-spacing: 2px;
        margin-bottom: -13px;
        margin-left: 20px;
      }

      & > input, > textarea, > div {
        background: #D9D9D9;
        color: var(--background);
        border: none;
        padding: 4px 8px;

        box-shadow: -6px 8px 0 #000;

        width: 100%;
        border-radius: 12px;
        font-size: .9rem;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 20px;

        resize: none;
        min-height: 34px;

        box-sizing: border-box;
      }

      & > div.genres {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding-block: 0;

        gap: 30px;

        padding-right: 100px;

        position: relative;

        & > div.genre {
          font-size: .76rem;
          letter-spacing: 0;
          font-weight: bold;

          display: flex;
          flex-direction: row;
          align-items: center;


          & > span {
            background: var(--background);
            color: #D9D9D9;
            padding: 0 4px;
            border-radius: 6px;
          }

          & > button {
            background: var(--background);
            color: red;
            border: none;
            padding: 0;

            margin-left: -8px;

            width: 34px;
            height: 34px;
            line-height: 48px;
            border-radius: 10px;

            scale: .54;
          }
        }

        & > button {
          background: var(--background);
          border: none;
          padding: 0 10px;
          border-radius: 6px;
          height: 16px;

          position: absolute;
          right: 10px;

          & > svg-icon {
            color: var(--secondary);;

            position: relative;
            top: -4px;
          }

        }
      }


    }
  }

}

</style>