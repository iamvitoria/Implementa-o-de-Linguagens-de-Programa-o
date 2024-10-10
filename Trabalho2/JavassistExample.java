import javassist.ClassPool;
import javassist.CtClass;
import javassist.CtField;
import javassist.CtMethod;
import javassist.CtNewMethod;
import javassist.Modifier;

public class JavassistExample {
    public static void main(String[] args) {
        try {
            ClassPool pool = ClassPool.getDefault();
            CtClass cc = pool.makeClass("MinhaClasse");

            // Adicionando um campo 'nome'
            CtField nomeField = new CtField(pool.get("java.lang.String"), "nome", cc);
            cc.addField(nomeField);

            // Adicionando método 'setNome'
            CtMethod setNomeMethod = CtNewMethod.make(
                "public void setNome(String nome) { this.nome = nome; }", cc);
            cc.addMethod(setNomeMethod);

            // Adicionando método 'getNome'
            CtMethod getNomeMethod = CtNewMethod.make(
                "public String getNome() { return this.nome; }", cc);
            cc.addMethod(getNomeMethod);

            // Criar a classe em tempo de execução
            Class<?> clazz = cc.toClass();
            Object obj = clazz.getDeclaredConstructor().newInstance();

            // Usar reflexão para chamar métodos
            clazz.getMethod("setNome", String.class).invoke(obj, "Vitória");
            String nome = (String) clazz.getMethod("getNome").invoke(obj);

            System.out.println("Nome: " + nome);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}