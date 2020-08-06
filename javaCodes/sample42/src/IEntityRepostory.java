public interface IEntityRepostory<T> {
    void add(T entity);
    void delete(T entity);
    void update(T entity);
}
