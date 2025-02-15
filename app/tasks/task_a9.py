from app.utils.file_utils import read_file_safe, write_file_safe
from sentence_transformers import SentenceTransformer, util

def run() -> str:
    """
    A9: Using embeddings, find the most similar pair of comments in /data/comments.txt
    and write them (one per line) to /data/comments-similar.txt.
    """
    # Read comments from the file, one comment per line
    comments_text = read_file_safe("comments.txt")
    comments = [line.strip() for line in comments_text.splitlines() if line.strip()]
    
    if len(comments) < 2:
        return "Not enough comments to compare."
    
    # Load a pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Compute embeddings for all comments
    embeddings = model.encode(comments, convert_to_tensor=True)
    
    # Compute pairwise cosine similarity matrix
    cosine_scores = util.cos_sim(embeddings, embeddings)
    
    # Initialize variables to track the best (most similar) pair
    max_score = -1
    best_pair = (None, None)
    n = len(comments)
    
    # Loop over pairs (only need to check each unique pair)
    for i in range(n):
        for j in range(i + 1, n):
            score = cosine_scores[i][j].item()
            if score > max_score:
                max_score = score
                best_pair = (comments[i], comments[j])
    
    # Prepare the output: each comment on a new line
    output = best_pair[0] + "\n" + best_pair[1]
    write_file_safe("comments-similar.txt", output)
    
    return f"Most similar pair found with cosine similarity {max_score:.4f}."