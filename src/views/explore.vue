<template>
    <div>
        <h1>Explore</h1>
        <div v-if="posts.length">
            <div v-for="post in posts" :key="post.id">
                <p>{{ post.caption }}</p>
                <img :src="post.photo" alt="post photo" />
                <p>By: <router-link :to="`/users/${post.user_id}`">{{ post.username }}</router-link></p>
            </div>
        </div>
        <div v-else>
            <p>No posts available.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            posts: [],
        };
    },
    mounted() {
        this.fetchPosts();
    },
    methods: {
        async fetchPosts() {
            try {
                const response = await axios.get('/api/v1/posts', {
                    headers: {
                        Authorization: `Bearer ${this.getAuthToken()}`,
                    },
                });
                this.posts = response.data;
            } catch (error) {
                console.error('Failed to fetch posts:', error);
            }
        },
        getAuthToken() {
            // Implement method to retrieve JWT token
            return localStorage.getItem('authToken');
        },
    },
};
</script>
<template>
    <div>
        <h1>Explore</h1>
        <div v-if="posts.length">
            <div v-for="post in posts" :key="post.id">
                <p>{{ post.caption }}</p>
                <img :src="post.photo" alt="post photo" />
                <p>By: <router-link :to="`/users/${post.user_id}`">{{ post.username }}</router-link></p>
            </div>
        </div>
        <div v-else>
            <p>No posts available.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            posts: [],
        };
    },
    mounted() {
        this.fetchPosts();
    },
    methods: {
        async fetchPosts() {
            try {
                const response = await axios.get('/api/v1/posts', {
                    headers: {
                        Authorization: `Bearer ${this.getAuthToken()}`,
                    },
                });
                this.posts = response.data;
            } catch (error) {
                console.error('Failed to fetch posts:', error);
            }
        },
        getAuthToken() {
            // Implement method to retrieve JWT token
            return localStorage.getItem('authToken');
        },
    },
};
</script>
