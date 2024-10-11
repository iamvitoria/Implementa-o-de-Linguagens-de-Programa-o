import javassist.ClassPool;
import javassist.CtClass;
import javassist.CtField;
import javassist.CtMethod;
import javassist.CtNewMethod;
import javassist.Modifier;

public class JavassistExample {
    public static void main(String[] args) {
        try {
            // Criação de uma nova classe usando Javassist
            ClassPool pool = ClassPool.getDefault();
            CtClass pessoaClass = pool.makeClass("Pessoa");

            // Adicionando um campo à classe
            CtField nomeField = new CtField(pool.get("java.lang.String"), "nome", pessoaClass);
            nomeField.setModifiers(Modifier.PRIVATE);
            pessoaClass.addField(nomeField, CtField.Initializer.constant("Sem nome"));

            // Adicionando métodos à classe
            CtMethod getNomeMethod = CtNewMethod.make("public String getNome() { return nome; }", pessoaClass);
            pessoaClass.addMethod(getNomeMethod);

            CtMethod setNomeMethod = CtNewMethod.make("public void setNome(String nome) { this.nome = nome; }", pessoaClass);
            pessoaClass.addMethod(setNomeMethod);

            // Testando a classe criada
            Class<?> pessoa = pessoaClass.toClass();
            Object pessoaInstance = pessoa.newInstance();
            pessoa.getMethod("setNome", String.class).invoke(pessoaInstance, "João");
            String nome = (String) pessoa.getMethod("getNome").invoke(pessoaInstance);
            System.out.println("Nome: " + nome); // Saída: Nome: João
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
