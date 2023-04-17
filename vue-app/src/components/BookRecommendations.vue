<template>
  <div>
    <div class="rectangle">
      <div class="notification-text">
        <a href="https://github.com/leammurphy/books-rs.git" class="made-link">How It's Made!</a>
      </div>
    </div>
    <!-- Input for the book title and the recommend button -->
    <div class="suggest">
      <input 
        v-model="bookTitle" 
        placeholder="Enter book title" 
        class="form-control" 
        ref="bookInput" 
        @click="resetRecommendations">
      <button 
        class="submit" 
        @click="getRecommendations">
          Recommend
      </button>
    </div>
    <!-- Display recommended books -->
    <div v-if="recommendations.length > 0" class="content">
      <h2>Recommended Books</h2>
      <p>{{ randomWord }}s who liked {{ bookTitle }} also liked these books!</p>
      
      <!-- Display recommended books in a carousel -->
      <carousel 
        :itemsToShow="2.5" 
        :wrapAround="true" 
        :transition="500">
          
        <!-- Loop through recommended books and create a slide for each -->
        <slide 
          v-for="book in recommendations" 
          :key="book.book_id" 
          id="book-container">
          <div class="carousel__item">
            <div class="book-image">
              <img :src="book.image_url" alt="Book cover">
            </div>
            <div class="book-details">
              <h4>{{ book.book_title }}</h4>
              <p>{{ book.authors }}</p>
              <p>{{ book.publication_year }}</p>
            </div>
          </div>
        </slide>
        
        <!-- Pagination and navigation controls for the carousel -->
        <template #addons>
          <Pagination />
          <Navigation />
        </template>
        
      </carousel> 
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue'
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation} from 'vue3-carousel'

export default defineComponent({
  // Component name
  name: 'BookRecommendations',
  // Register component sub-components
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation
  },
  // Component data properties
  data: () => ({
    bookTitle: '', // Input for the book title
    recommendations: [], // Array of recommended books
    words: ['Bookworm', 'Bibliophile', 'Avid reader', 'Literary enthusiast', 'Page-turner', 
            'Bibliophile', 'Bookworm', 'Reader', 'Book lover', 'Literary aficionado', 
            'Page-turner addict', 'Bibliomaniac', 'Reading enthusiast', 'Bibliophilic individual', 'Bookish person', 
            'Literature lover', 'Reading addict', 'Book aficionado', 'Print nerd', 'Tome enthusiast', 
            'Wordsmith', 'Literary connoisseur', 'Reading fanatic', 'Book connoisseur', 'Library fiend', 
            'Bookaholic','Book nerd','Book addict', 'Book devotee','Reading zealot', 
            'Ink fiend', 'Book enthusiast', 'Literary addict', 'Bookhound', 'Bibliognost'
          ],
    randomWord: '', // Random word to display as a label
  }),
  // Component methods
  methods: {
    // HTTP request to get book recommendations
    getRecommendations() {
      axios.get('http://127.0.0.1:5000/recommendations', {
          params: {
              book_title: this.bookTitle
          }
      })
      .then(response => {
        // Save the retrieved book recommendations
        this.recommendations = response.data.nearest_neighbors;
      })
      .catch(error => {
        console.log(error);
      });

      // Pick a random word from the array and save it
      const randomIndex = Math.floor(Math.random() * this.words.length);
      this.randomWord = this.words[randomIndex];
    },

    // Clear the input and recommendations array
    resetRecommendations() {
      this.recommendations = [];
      this.randomWord = '';
      this.bookTitle = "";
    },
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');
/* Set font family and size for headers and text */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Raleway', serif;
  font-weight: bold;
}
p, input {
  font-family: 'Raleway', serif;
  font-size: 18px;
}
/* Style for recommend button */
.submit {
  font-family: 'Raleway', serif;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  display:inline-block;
  width:100px;
  height:40px;
  line-height:40px;
  border:0px solid white;
  text-transform: capitalize;
  border-radius:2px;
  position:relative;
  overflow:hidden;
  padding: 0;
}
.submit:active {
  transform: scale(0.85);
}.submit:before{
  transition: all 0.1s linear;  
  display:block; 
}.submit:after {
  transition: all 0.3s ease-in-out;  
  content: "";
  display: block;
  background-color:#6E1938;
  margin-top:0px;
  height: 40px;
}
.submit:hover:after{
    margin-top:-40px;
}
.submit:hover{
    color: #ebe8de;;
}

.form-control {
  transition: .25s border ease-in-out;
  border-radius: 0 !important;
  outline: none !important;
  box-shadow: none !important;
  background: transparent;
  color: black;
  border: 0;
  border-bottom: 2px solid #444;
  font-size: 20px;
  margin-right: 10px;
  height:40px;
}

.form-control:focus {
  border-bottom-color: #6E1938;
}

.content {
  width: 55%;
  margin: 0 auto; /* This centers the div horizontally */
}
/* Style for book title */
.book-image img {
  display: block;
  margin: 0 auto;
  width: 175px;
  height: 250px;
  margin-top: 15px;
}
/* Style for book details */
.book-details {
  font-size: 20px;
}

/* Style for carousel item container */
.carousel__slide {
  padding: 5px;
  border-radius: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 200px;
  height: 400px;
  position: relative;
  background-color: #496462;
}

.carousel__viewport {
  perspective: 2000px;
}

.carousel__track {
  transform-style: preserve-3d;
}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  opacity: 0.6;
  transform: rotateY(-20deg) scale(0.85);
}

.carousel__slide--active ~ .carousel__slide {
  transform: rotateY(20deg) scale(0.85);
}

.carousel__slide--prev {
  opacity: .6;
  transform: rotateY(-10deg) scale(0.9);
  filter: blur(10px);
}

.carousel__slide--next {
  opacity: .6;
  transform: rotateY(10deg) scale(0.9);
  filter: blur(10px);
}

.carousel__slide--active {
  opacity: 1;
  transform: rotateY(0) scale(1);
  
}
.rectangle {
  position: absolute;
  top: 0;
  right: 0;
  margin: 20px;

  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 50px;
  height: 50px;
  background: #6E1938;
  transform: scale(0);
  border-radius: 50%;
  color: #F0F0F0;
  opacity: 0;
  overflow: hidden;
  animation: scale-in .3s ease-out forwards,
    expand .35s .25s ease-out forwards;
  animation-delay: 5s;
}
.made-link {
  font-family: 'Raleway', serif;
  font-weight: bold;
  transition: all 0.3s ease-in-out;
  display:inline-block;
  width:150px;
  height:40px;
  line-height:40px;
  border:0px solid white;
  text-transform: capitalize;
  border-radius:2px;
  position:relative;
  overflow:hidden;
  padding: 0;
  position: relative;
  font-size: 14px;
  font-weight: bold;
  color: black;
  background-color: #F0F0F0;
  border: 2px solid #6E1938;
  text-align: center;
  text-decoration: none;
  border-radius: 5px;
}
.made-link:active {
  transform: scale(0.85);
}.made-link:before{
  transition: all 0.1s linear;  
  display:block; 
}.made-link:after {
  transition: all 0.3s ease-in-out;  
  content: "";
  display: block;
  background-color:#6E1938;
  margin-top:0px;
  height: 40px;
}
.made-link:hover:after{
    margin-top:-40px;
}
.made-link:hover{
    color: #ebe8de;;
}

.notification-text {
  display: flex;
  align-items: center;
  padding: 0 16px;
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  animation: fade-in .65s ease-in forwards;
}



@keyframes scale-in {
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes expand {
  50% {
    width: 350px;
    border-radius: 6px;
  }
  100% {
    width: 300px;
    border-radius: 4px;
    box-shadow: 0px 1px 3px 0px rgba(0,0,0,.2),
                0px 1px 1px 0px rgba(0,0,0,.14),
                0px 3px 3px -1px rgba(0,0,0,.12);
  }
}

@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: .8;
  }
}


@media (max-width: 768px) {
  .content {
    width: 90%;
  }
  
  .carousel__slide {
    width: 150px;
    height: 300px;
  }
  
  p, input {
    font-size: 16px;
  }
  .book-image img {
    width: 50%;
    height: auto;
  }
  .submit {
    width: 80px;
    height: 30px;
    line-height: 30px;
    font-size: 12px;
  }
}
</style>
