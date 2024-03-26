#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 256
#define CACHE_SLOTS_MIN 100
#define CACHE_SLOTS_MAX 1000
#define CACHE_SLOTS_STEP 100


typedef struct Node {
    char *page;
    struct Node *next;
    struct Node *prev;
} Node;


typedef struct {
    Node *head;
    Node *tail;
    int cache_slots;
    int cache_hit;
    int tot_cnt;
} CacheSimulator;

void initCacheSimulator(CacheSimulator *cache_sim, int slots) {
    cache_sim->cache_slots = slots;
    cache_sim->cache_hit = 0;
    cache_sim->tot_cnt = 0;
    cache_sim->head = NULL;
    cache_sim->tail = NULL;
}

Node *createNode(const char *page) {
    Node *node = (Node *)malloc(sizeof(Node));
    if (node != NULL) {
        node->page = strdup(page);
        node->next = NULL;
        node->prev = NULL;
    }
    return node;
}

void do_sim(CacheSimulator *cache_sim, const char *page) {
    cache_sim->tot_cnt++;

    Node *current = cache_sim->head;
    while (current != NULL) {
        if (strcmp(current->page, page) == 0) {
            cache_sim->cache_hit++;
            if (current != cache_sim->head) {

                if (current->prev != NULL) {
                    current->prev->next = current->next;
                }
                if (current->next != NULL) {
                    current->next->prev = current->prev;
                }
                current->next = cache_sim->head;
                if (cache_sim->head != NULL) {
                    cache_sim->head->prev = current;
                }
                cache_sim->head = current;
                if (cache_sim->tail == current) {
                    cache_sim->tail = current->prev;
                }
                current->prev = NULL;
            }
            return;
        }
        current = current->next;
    }

    if (cache_sim->cache_slots <= cache_sim->tot_cnt) {
        Node *temp = cache_sim->tail;
        if (temp != NULL) {
            free(temp->page);
            free(temp);
            if (cache_sim->tail->prev != NULL) {
                cache_sim->tail->prev->next = NULL;
                cache_sim->tail = cache_sim->tail->prev;
            } else {
                cache_sim->head = NULL;
                cache_sim->tail = NULL;
            }
        }
    }

    Node *node = createNode(page);
    if (node != NULL) {
        node->next = cache_sim->head;
        if (cache_sim->head != NULL) {
            cache_sim->head->prev = node;
        }
        cache_sim->head = node;
        if (cache_sim->tail == NULL) {
            cache_sim->tail = node;
        }
    }
}

void print_stats(CacheSimulator *cache_sim) {
    printf("cache_slot = %d cache_hit = %d hit ratio = %f\n", cache_sim->cache_slots, cache_sim->cache_hit, (double)cache_sim->cache_hit / cache_sim->tot_cnt);
}

int main() {

    FILE *data_file = fopen("./linkbench.trc", "r");
    if (data_file == NULL) {
        perror("Error: Unable to open the file.");
        return 1;
    }
    int cache_slots;
    for (cache_slots = CACHE_SLOTS_MIN; cache_slots <= CACHE_SLOTS_MAX; cache_slots += CACHE_SLOTS_STEP) {
        CacheSimulator cache_sim;
        initCacheSimulator(&cache_sim, cache_slots);
        char line[MAX_LINE_LENGTH];

        while (fgets(line, sizeof(line), data_file)) {
            char *page = strtok(line, " ");
            do_sim(&cache_sim, page);
        }

        print_stats(&cache_sim);


        rewind(data_file);
    }
    fclose(data_file);

    return 0;
}
